(function () {
  function initNavbar() {
    const navbar = document.querySelector(".navbar.sticky-top");
    if (!navbar) {
      return;
    }

    let isScrolled = false;

    const setOffset = () => {
      const height = Math.ceil(navbar.getBoundingClientRect().height);
      document.documentElement.style.setProperty("--navbar-offset", `${height}px`);
    };

    const updateScroll = () => {
      const top = window.scrollY;
      if (top > 10 && !isScrolled) {
        navbar.classList.add("scrolled");
        isScrolled = true;
      } else if (top <= 10 && isScrolled) {
        navbar.classList.remove("scrolled");
        isScrolled = false;
      }
    };

    updateScroll();
    setOffset();

    window.addEventListener("resize", setOffset, { passive: true });
    window.addEventListener(
      "scroll",
      () => {
        window.requestAnimationFrame(updateScroll);
      },
      { passive: true }
    );
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initNavbar);
  } else {
    initNavbar();
  }
})();
