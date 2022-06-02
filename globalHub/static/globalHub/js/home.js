var requestQuote = document.querySelector("#request-quote");
var requestQuoteButton = document.querySelector("#request-quote-button");

requestQuoteButton.addEventListener("click", navigateToRequestQuote, false);

function navigateToRequestQuote(e) {
  console.log("navigateToRequestQuote");
  requestQuote.scrollIntoView({ behavior: "smooth" });
}
