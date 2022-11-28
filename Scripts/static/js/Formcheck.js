const Searchinput = document.getElementById("Search1");

Searchinput.addEventListener("input", (event) => {
  if (Searchinput.validity.valueMissing) {
    Searchinput.setCustomValidity("I am the Javascript, I ran because the form was left empty, Hi there");
    Searchinput.reportValidity();
  } else {
    Searchinput.setCustomValidity("");
  }
});