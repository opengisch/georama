(function () {
  try {
    const root = document.documentElement;
    const defaultTheme = root.getAttribute("data-theme-default") || "light";
    const saved = localStorage.getItem("theme");
    const prefersDark =
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches;
    let theme = saved;

    if (theme !== "light" && theme !== "dark") {
      if (defaultTheme === "auto") {
        theme = prefersDark ? "dark" : "light";
      } else {
        theme = defaultTheme === "dark" ? "dark" : "light";
      }
    }

    root.setAttribute("data-bs-theme", theme);
  } catch (err) {
    // Ignore theme initialization failures (e.g., storage blocked).
  }
})();
