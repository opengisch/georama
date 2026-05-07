#!/bin/bash

# ==============================================================================
#  GEORAMA LOCAL SETUP SCRIPT
#  For Ubuntu 24.04 — Local testing only
# ==============================================================================

set -euo pipefail

# ==============================================================================
#  ✏️  USER CONFIGURATION — EDIT THESE VARIABLES BEFORE RUNNING
# ==============================================================================

GITHUB_USERNAME="your_github_username"
GITHUB_TOKEN="ghp_your_personal_access_token"

# Where the Georama source code will be downloaded (folder must already exist)
INSTALL_DIR="$HOME/git"

# Where your QGIS projects live (folder must already exist)
QGIS_DATA_DIR="$HOME/georama-data"

# Password for the Georama admin account (username is always 'admin')
GEORAMA_ADMIN_PASSWORD="your_admin_password"

# ==============================================================================
#  DO NOT EDIT BELOW THIS LINE
# ==============================================================================

GEORAMA_DIR="$INSTALL_DIR/georama"
REPO_URL="https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/opengisch/georama.git"

# ------------------------------------------------------------------------------
#  Colors & formatting
# ------------------------------------------------------------------------------
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# ------------------------------------------------------------------------------
#  Logging helpers
# ------------------------------------------------------------------------------
log()     { echo -e "${CYAN}[INFO]${RESET}  $1"; }
success() { echo -e "${GREEN}[OK]${RESET}    $1"; }
warn()    { echo -e "${YELLOW}[WARN]${RESET}  $1"; }
error()   { echo -e "${RED}[ERROR]${RESET} $1"; }
step()    { echo -e "\n${BOLD}━━━  $1${RESET}"; }

# ------------------------------------------------------------------------------
#  Error trap
# ------------------------------------------------------------------------------
trap 'error "An unexpected error occurred on line $LINENO. Setup aborted."; exit 1' ERR

# ------------------------------------------------------------------------------
#  Warning banner
# ------------------------------------------------------------------------------
print_warning() {
echo ""
echo -e "${YELLOW}${BOLD}"
echo "  ╔══════════════════════════════════════════════════════════════════════╗"
echo "  ║                        ⚠️   WARNING  ⚠️                               ║"
echo "  ║                                                                      ║"
echo "  ║  This script sets up Georama for LOCAL TESTING ONLY.                 ║"
echo "  ║                                                                      ║"
echo "  ║  • It uses development settings (debug mode ON, default passwords,   ║"
echo "  ║    no HTTPS, no real authentication).                                ║"
echo "  ║  • It is NOT suitable for production or public-facing deployments.   ║"
echo "  ║  • This script is provided as-is, with no warranty of any kind.      ║"
echo "  ║  • The authors take no responsibility for anything that goes wrong.  ║"
echo "  ║                                                                      ║"
echo "  ║  If you need a production setup, refer to the official Georama docs. ║"
echo "  ╚══════════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"
}

# ==============================================================================
#  START
# ==============================================================================

print_warning

echo ""
log "Starting Georama local setup..."
echo ""

# ------------------------------------------------------------------------------
#  STEP 1 — Validate user configuration
# ------------------------------------------------------------------------------
step "STEP 1 — Checking configuration variables"

CONFIG_OK=true

if [[ "$GITHUB_USERNAME" == "your_github_username" || -z "$GITHUB_USERNAME" ]]; then
    error "GITHUB_USERNAME is not set. Please edit the script and set your GitHub username."
    CONFIG_OK=false
fi

if [[ "$GITHUB_TOKEN" == "ghp_your_personal_access_token" || -z "$GITHUB_TOKEN" ]]; then
    error "GITHUB_TOKEN is not set. Please edit the script and set your GitHub Personal Access Token."
    CONFIG_OK=false
fi

if [[ -z "$INSTALL_DIR" ]]; then
    error "INSTALL_DIR is not set. Please edit the script and set the folder where the code should be downloaded."
    CONFIG_OK=false
elif [[ ! -d "$INSTALL_DIR" ]]; then
    error "INSTALL_DIR does not exist: $INSTALL_DIR"
    error "Please create it first:  mkdir -p \"$INSTALL_DIR\""
    CONFIG_OK=false
else
    success "INSTALL_DIR exists: $INSTALL_DIR"
fi

if [[ -z "$QGIS_DATA_DIR" ]]; then
    error "QGIS_DATA_DIR is not set. Please edit the script and set the folder where your QGIS projects live."
    CONFIG_OK=false
elif [[ ! -d "$QGIS_DATA_DIR" ]]; then
    error "QGIS_DATA_DIR does not exist: $QGIS_DATA_DIR"
    error "Please create it first:  mkdir -p \"$QGIS_DATA_DIR\""
    CONFIG_OK=false
else
    success "QGIS_DATA_DIR exists: $QGIS_DATA_DIR"
fi

if [[ "$GEORAMA_ADMIN_PASSWORD" == "your_admin_password" || -z "$GEORAMA_ADMIN_PASSWORD" ]]; then
    error "GEORAMA_ADMIN_PASSWORD is not set. Please edit the script and set a password for the admin account."
    CONFIG_OK=false
fi

if [[ "$CONFIG_OK" == false ]]; then
    echo ""
    error "One or more configuration variables are missing or invalid."
    error "Please open this script in a text editor, fix the variables at the top, and run it again."
    exit 1
fi

success "All configuration variables look good."

# ------------------------------------------------------------------------------
#  STEP 2 — Install system dependencies
# ------------------------------------------------------------------------------
step "STEP 2 — Installing system dependencies"

log "Updating package list..."
sudo apt-get update -qq

log "Installing Git..."
sudo apt-get install -y -qq git

success "System dependencies installed."

# ------------------------------------------------------------------------------
#  STEP 3 — Install Docker
# ------------------------------------------------------------------------------
step "STEP 3 — Installing Docker"

if command -v docker &>/dev/null; then
    success "Docker is already installed: $(docker --version)"
else
    log "Docker not found. Installing..."

    sudo apt-get remove -y docker docker-engine docker.io containerd runc 2>/dev/null || true
    sudo apt-get install -y -qq ca-certificates curl gnupg

    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
      https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt-get update -qq
    sudo apt-get install -y -qq docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    success "Docker installed."
fi

# Determine whether to use plain 'docker' or 'sudo docker'
# We test actual socket access rather than relying on group membership,
# which may not be active yet without a logout/login.
if docker info &>/dev/null 2>&1; then
    DOCKER="docker"
    success "Docker is accessible without sudo."
elif sudo docker info &>/dev/null 2>&1; then
    DOCKER="sudo docker"
    warn "Docker requires sudo for this session. Adding '$USER' to the docker group"
    warn "so this won't be needed after your next login."
    sudo usermod -aG docker "$USER"
else
    error "Cannot connect to the Docker daemon even with sudo."
    error "Please check that Docker is running:  sudo systemctl status docker"
    exit 1
fi

# ------------------------------------------------------------------------------
#  STEP 4 — Clone the repository
# ------------------------------------------------------------------------------
step "STEP 4 — Cloning Georama repository"

if [[ -d "$GEORAMA_DIR/.git" ]]; then
    success "Georama repository already exists at $GEORAMA_DIR — skipping clone."
else
    log "Cloning from GitHub into $GEORAMA_DIR ..."
    if ! git clone "$REPO_URL" "$GEORAMA_DIR"; then
        error "Failed to clone the repository."
        error "Please check that your GITHUB_USERNAME and GITHUB_TOKEN are correct,"
        error "and that your account has been granted access to the repository."
        exit 1
    fi
    success "Repository cloned successfully."
fi

cd "$GEORAMA_DIR"

# ------------------------------------------------------------------------------
#  STEP 5 — Configure .env
# ------------------------------------------------------------------------------
step "STEP 5 — Configuring environment"

if [[ ! -f ".env" ]]; then
    log "Creating .env from example..."
    cp .env.dev.example .env
    success ".env file created."
else
    success ".env file already exists — keeping it."
fi

# Set GEORAMA_LOCAL_DATA
if grep -q "^GEORAMA_LOCAL_DATA=" .env; then
    sed -i "s|^GEORAMA_LOCAL_DATA=.*|GEORAMA_LOCAL_DATA=$QGIS_DATA_DIR|" .env
else
    echo "GEORAMA_LOCAL_DATA=$QGIS_DATA_DIR" >> .env
fi
success "GEORAMA_LOCAL_DATA set to: $QGIS_DATA_DIR"

# Set GEORAMA_DATA_INTEGRATION_ROOT to the container-internal path
if grep -q "^GEORAMA_DATA_INTEGRATION_ROOT=" .env; then
    sed -i "s|^GEORAMA_DATA_INTEGRATION_ROOT=.*|GEORAMA_DATA_INTEGRATION_ROOT=/io/data|" .env
else
    echo "GEORAMA_DATA_INTEGRATION_ROOT=/io/data" >> .env
fi
success "GEORAMA_DATA_INTEGRATION_ROOT set to: /io/data"

# ------------------------------------------------------------------------------
#  STEP 6 — Build Docker containers
# ------------------------------------------------------------------------------
step "STEP 6 — Building Docker containers (this may take 10–15 minutes)"

log "Running: docker compose build"
if ! $DOCKER compose build; then
    error "Docker build failed. Check the output above for details."
    exit 1
fi
success "Docker containers built successfully."

# ------------------------------------------------------------------------------
#  STEP 7 — Start services
# ------------------------------------------------------------------------------
step "STEP 7 — Starting Georama services"

log "Running: docker compose up -d"
if ! $DOCKER compose up -d; then
    error "Failed to start Docker services. Check the output above for details."
    exit 1
fi
success "All services started."

# ------------------------------------------------------------------------------
#  STEP 8 — Wait for services to be ready
# ------------------------------------------------------------------------------
step "STEP 8 — Waiting for services to be ready"

log "Waiting for the database to become healthy..."
RETRIES=30
until $DOCKER compose exec -T georama-db pg_isready -U postgres -d postgres &>/dev/null; do
    RETRIES=$((RETRIES - 1))
    if [[ $RETRIES -eq 0 ]]; then
        error "Database did not become ready in time. Check: $DOCKER compose logs georama-db"
        exit 1
    fi
    log "Still waiting... ($RETRIES attempts left)"
    sleep 3
done
success "Database is ready."

# ------------------------------------------------------------------------------
#  STEP 9 — Run migrations
# ------------------------------------------------------------------------------
step "STEP 9 — Running database migrations"

log "Running: docker compose exec georama make migrate"
if ! $DOCKER compose exec -T georama make migrate; then
    error "Database migration failed. Check the output above for details."
    exit 1
fi
success "Migrations applied."

# ------------------------------------------------------------------------------
#  STEP 10 — Create superuser
# ------------------------------------------------------------------------------
step "STEP 10 — Creating admin user"

log "Running: docker compose exec georama make create-superuser"
log "You will be prompted to set a password for the 'admin' user."
echo ""
if ! echo "$GEORAMA_ADMIN_PASSWORD" | $DOCKER compose exec -T georama python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
import sys
password = sys.stdin.readline().strip()
if User.objects.filter(username='admin').exists():
    u = User.objects.get(username='admin')
    u.set_password(password)
    u.save()
    print('Admin password updated.')
else:
    User.objects.create_superuser('admin', 'admin@localhost', password)
    print('Admin user created.')
"; then
    error "Superuser creation failed. Check the output above for details."
    exit 1
fi
success "Admin user created."

# ------------------------------------------------------------------------------
#  STEP 11 — Load example content
# ------------------------------------------------------------------------------
step "STEP 11 — Loading example content"

log "Running: docker compose exec georama make create-example-content"
if ! $DOCKER compose exec -T georama make create-example-content; then
    warn "Example content loading failed or was already loaded — continuing anyway."
fi
success "Example content step complete."

# ==============================================================================
#  DONE
# ==============================================================================

print_warning

echo ""
echo -e "${GREEN}${BOLD}"
echo "  ╔══════════════════════════════════════════════════════════════════════╗"
echo "  ║                     🎉  Setup complete!                              ║"
echo "  ║                                                                      ║"
echo "  ║  Georama is now running locally. Open your browser and go to:        ║"
echo "  ║                                                                      ║"
echo "  ║       👉   http://localhost:4242/                                    ║"
echo "  ║                                                                      ║"
echo "  ║  Log in with:                                                        ║"
echo "  ║    Username : admin                                                  ║"
echo "  ║    Password : (the one you just set)                                 ║"
echo "  ║                                                                      ║"
echo "  ║  To stop Georama:   cd $GEORAMA_DIR"
echo "  ║                     $DOCKER compose down                              ║"
echo "  ║                                                                      ║"
echo "  ║  To start it again: $DOCKER compose up -d                             ║"
echo "  ╚══════════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"
