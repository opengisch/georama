(function () {
  const icon = document.getElementById("themeIcon");
  const toggle = document.getElementById("themeToggle");
  const defaultTheme =
    document.documentElement.getAttribute("data-theme-default") || "light";

  function resolveTheme() {
    const saved = localStorage.getItem("theme");
    if (saved === "light" || saved === "dark") {
      return saved;
    }
    if (defaultTheme === "auto") {
      return window.matchMedia &&
        window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
    }
    return defaultTheme === "dark" ? "dark" : "light";
  }

  function updateIcon() {
    if (!icon) {
      return;
    }
    const current = document.documentElement.getAttribute("data-bs-theme");
    icon.className =
      current === "dark" ? "fa fa-solid fa-sun" : "fa fa-solid fa-moon";
  }

  function applyTheme(theme) {
    const next = theme === "dark" ? "dark" : "light";
    document.documentElement.setAttribute("data-bs-theme", next);
    localStorage.setItem("theme", next);
    updateIcon();
  }

  const initial = resolveTheme();
  document.documentElement.setAttribute("data-bs-theme", initial);
  updateIcon();

  if (toggle) {
    toggle.addEventListener("click", () => {
      const current =
        document.documentElement.getAttribute("data-bs-theme") || "light";
      applyTheme(current === "dark" ? "light" : "dark");
    });
  }
})();
