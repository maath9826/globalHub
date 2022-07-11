import { env } from "./env.js";

var contactEl = document.querySelector("#contact");

// request quote

var form = document.querySelector("#contact form");
var submitButton = document.querySelector("#contact button[type='submit']");
var spinner = document.querySelector("#contact form .spinner-border");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  startLoading();

  let formData = new FormData(form);
  let formMap = {};
  for (var [key, value] of formData) {
    formMap[key] = value;
  }

  fetch(`${env.serverUrl}/contact/create`, {
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
  var toastEl = document.querySelector("#contact-toast");
  let toast = new bootstrap.Toast(toastEl);
  toast.show();
}
