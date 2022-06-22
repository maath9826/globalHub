var nav_items = document.querySelectorAll(".nav_item");
var services = document.querySelectorAll(".service .title");
var serviceTitles = document.querySelectorAll(".service .title");
var destination_service = document.querySelector("#destination_service");

document.addEventListener("DOMContentLoaded", (event) => {
  if (destination_service) {
    destination_service.scrollIntoView({ behavior: "smooth" });
  }
});

for (let i = 0; i < nav_items.length; i++) {
  nav_items[i].addEventListener(
    "click",
    (e) => {
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
