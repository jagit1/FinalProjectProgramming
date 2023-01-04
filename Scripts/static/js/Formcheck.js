const Searchinput = document.getElementById("Search1");

Searchinput.addEventListener("input", (event) => {
  if (Searchinput.validity.valueMissing) {
    Searchinput.setCustomValidity("Please fill in this Field");
    Searchinput.reportValidity();
  } else {
    Searchinput.setCustomValidity("");
  }
});