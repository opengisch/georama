# hepler to prepare certificates for the dev stack (keycloak, geogirafe) meant to be run
# as oneshot service `certs` in compose.yml before the services which use them are started
#
# - the certificate authority is kept in CA_DIR (docker volume), it is only created again
#   when it is missing or expires, then it has to be trusted again
# - the certificate is kept in CERTS_DIR (bind mount), it is created again when it is
#   missing, expires, its config changed or the certificate authority was renewed

CA_DIR ?= /ca
CERTS_DIR ?= /certs
TMP_DIR ?= /tmp
UID ?= 1000
GID ?= 1000

CA_DAYS = 3650
# macOS rejects TLS certificates which are valid for more than 825 days
CERT_DAYS = 825
RENEW_BEFORE_SECONDS = 2592000

CA_KEY = $(CA_DIR)/rootCA.key
CA_CERT = $(CA_DIR)/rootCA.crt
TRUSTED_CA_CERT = $(CERTS_DIR)/rootCA.crt
CERT = $(CERTS_DIR)/localhost.crt
CERT_KEY = $(CERTS_DIR)/localhost.key
# lighttpd (geogirafe) expects key and certificate in one file
CERT_PEM = $(CERTS_DIR)/localhost.pem

.PHONY: all expire certificates permissions

all:
	@$(MAKE) --no-print-directory expire
	@$(MAKE) --no-print-directory certificates permissions

# removes what expires soon, so that the file targets create it again
expire:
	@for cert in $(CA_CERT) $(CERT); do \
		if [ -f $$cert ] && ! openssl x509 -in $$cert -noout -checkend $(RENEW_BEFORE_SECONDS) > /dev/null; then \
			echo "$$cert expires soon, renewing."; \
			rm -f $$cert; \
		fi; \
	done
	@if [ ! -f $(CA_KEY) ]; then rm -f $(CA_CERT); fi

certificates: $(TRUSTED_CA_CERT) $(CERT_PEM)

$(CA_CERT): ca.cnf
	@echo "Creating certificate authority, trust $(TRUSTED_CA_CERT) (again)."
	@mkdir -p $(CA_DIR)
	openssl req -x509 -newkey rsa:4096 -nodes -sha256 -days $(CA_DAYS) \
		-config ca.cnf -keyout $(CA_KEY) -out $@

$(TRUSTED_CA_CERT): $(CA_CERT)
	@mkdir -p $(CERTS_DIR)
	cp $< $@

$(CERT): $(CA_CERT) localhost.cnf
	@echo "Creating certificate."
	@mkdir -p $(CERTS_DIR)
	openssl req -new -newkey rsa:2048 -nodes -sha256 \
		-config localhost.cnf -keyout $(CERT_KEY) -out $(TMP_DIR)/localhost.csr
	openssl x509 -req -sha256 -days $(CERT_DAYS) -in $(TMP_DIR)/localhost.csr \
		-CA $(CA_CERT) -CAkey $(CA_KEY) \
		-CAserial $(TMP_DIR)/rootCA.srl -CAcreateserial \
		-extfile localhost.cnf -extensions localhost_ext -out $@

$(CERT_PEM): $(CERT)
	cat $(CERT_KEY) $(CERT) > $@

# the services read the files with their own users, dev only!
# the files are handed over to the host user (no effect on macOS/Windows)
permissions:
	@chmod 644 $(CERTS_DIR)/*
	@chown -R $(UID):$(GID) $(CERTS_DIR) 2> /dev/null || true
