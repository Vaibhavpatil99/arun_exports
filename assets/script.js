// document.body.children[0].addEventListener("click", event => {
//   const nav = document.querySelector("nav");
//   const header = document.querySelector("header");

//   if (event.target.dataset.menustate == "closed") {
//     event.target.dataset.menustate = nav.dataset.state = header.dataset.menustate =
//       "open";
//   } else {
//     event.target.dataset.menustate = nav.dataset.state = header.dataset.menustate =
//       "closed";
//   }
// });

document.addEventListener("DOMContentLoaded", function() {
  const menuButton = document.querySelector(".nav-toggle");
  const nav = document.querySelector("nav");
  const header = document.querySelector("header");

  menuButton.addEventListener("click", function(event) {
    const menuState = menuButton.getAttribute("data-menustate");

    if (menuState === "closed") {
      menuButton.setAttribute("data-menustate", "open");
      nav.setAttribute("data-state", "open");
      header.setAttribute("data-menustate", "open");
    } else {
      menuButton.setAttribute("data-menustate", "closed");
      nav.setAttribute("data-state", "closed");
      header.setAttribute("data-menustate", "closed");
    }
  });
});
