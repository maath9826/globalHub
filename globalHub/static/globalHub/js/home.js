import { env } from "./env.js";

var requestQuote = document.querySelector("#request-quote");
var requestQuoteButton = document.querySelector("#request-quote-button");

requestQuoteButton.addEventListener("click", navigateToRequestQuote, false);

function navigateToRequestQuote(e) {
  requestQuote.scrollIntoView({ behavior: "smooth" });
}

// request quote

var form = document.querySelector("#request-quote form");
var submitButton = document.querySelector(
  "#request-quote button[type='submit']"
);
var spinner = document.querySelector("#request-quote form .spinner-border");
// var toast = document.querySelector("#request-quote #toast");
var dropdownToggle = document.querySelector("#request-quote .dropdown-toggle");
var dropdownItems = document.querySelectorAll("#request-quote .dropdown-item");

dropdownItems.forEach((el) => {
  el.addEventListener("click", (e) => {
    let freightType = form.querySelector("input[name=freightType]");
    freightType.value = e.target.dataset.id;

    let dropdownInnerElements = dropdownToggle.innerHTML.split("\n");
    dropdownInnerElements[1] = e.target.innerHTML;
    dropdownToggle.innerHTML = dropdownInnerElements.join("\n");

    dropdownInnerElements;
  });
});

form.addEventListener("submit", (e) => {
  e.preventDefault();

  startLoading();

  let formData = new FormData(form);
  let formMap = {};
  for (var [key, value] of formData) {
    formMap[key] = value;
  }
  formMap["fragile"] = formMap["fragile"] ? true : false;
  formMap["expressDelivery"] = formMap["expressDelivery"] ? true : false;
  formMap["insurance"] = formMap["insurance"] ? true : false;
  formMap["packaging"] = formMap["packaging"] ? true : false;

  fetch(`${env.serverUrl}/quote/create`, {
    method: "post",
    body: JSON.stringify(formMap),
  }).then((res) => {
    if (res.status != 200) {
      finishLoading();
    } else {
      res.json().then((data) => {
        finishLoading();
        showToast();
      });
    }
  });
});

function startLoading() {
  submitButton.classList.add("d-none");
  spinner.classList.remove("d-none");
}

function finishLoading() {
  submitButton.classList.remove("d-none");
  spinner.classList.add("d-none");
}

function showToast() {
  var toastEl = document.querySelector("#quote-toast");
  let toast = new bootstrap.Toast(toastEl);
  toast.show();
}
