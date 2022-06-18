var nav_items = document.querySelectorAll(".nav_item");
var services = document.querySelectorAll(".service .title");
var serviceTitles = document.querySelectorAll(".service .title");

for (let i = 0; i < nav_items.length; i++) {
  nav_items[i].addEventListener(
    "click",
    (e) => {
      console.log("navigateToService");
      services[i].scrollIntoView({ behavior: "smooth" });
    },
    false
  );
}

document.addEventListener(
  "scroll",
  function () {
    for (let i = 0; i < nav_items.length; i++) {
      if (isInViewport(serviceTitles[i])) {
        nav_items[i].classList.add(["viewport-service"]);
      } else {
        nav_items[i].classList.remove(["viewport-service"]);
      }
    }
  },
  {
    passive: true,
  }
);

function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <=
      (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// function navigateToService(e, el) {
//   console.log("navigateToService");
//   el.scrollIntoView({ behavior: "smooth" });
// }
