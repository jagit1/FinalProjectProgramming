var countries = ["Afghanistan","Albania", "Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia (Plur. State of)","Bosnia and Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei Darussalam","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Cayman Islands","Central African Rep.","Chad","Chile" ,"China", "China, Hong Kong SAR" ,"China, Macao SAR","Colombia","Comoros","Congo" ,"Cook Islands" ,"Costa Rica" ,"Cï¿½te d'Ivoire" ,"Croatia" ,"Cuba" ,"Curaï¿½ao" ,"Cyprus" ,"Czechia" ,"Dem. Rep. of the Congo", "Denmark", "Djibouti","Dominica", "Dominican Republic" ,"Ecuador" ,"Egypt", "El Salvador" ,"Equatorial Guinea" ,"Eritrea" ,"Ethiopia" ,"Estonia" ,"Eswatini" ,"Faeroe Islands" ,"Falkland Is. (Malvinas)" ,"Fiji" ,"Finland" ,"France" ,"French Guiana" ,"French Polynesia", "Gabon" ,"Gambia" ,"Georgia" ,"Germany", "Ghana" ,"Gibraltar" ,"Greece" ,"Greenland" ,"Grenada" ,"Guadeloupe" ,"Guam" ,"Guatemala" ,"Guernsey" ,"Guinea" ,"Guinea-Bissau" ,"Guyana" ,"Haiti" ,"Honduras" ,"Hungary" ,"Iceland" ,"India" ,"Indonesia" ,"Iran (Islamic Rep. of)", "Iraq" ,"Ireland", "Israel" ,"Italy" ,"Jamaica" ,"Japan" ,"Jersey" ,"Jordan" ,"Kazakhstan" ,"Kenya" ,"Kiribati" ,"Korea, Dem.Ppl's.Rep." ,"Korea, Republic of" ,"Kosovo" ,"Kuwait" ,"Kyrgyzstan" , "Lao People's Dem. Rep." ,"Latvia" ,"Lebanon" ,"Lesotho" ,"Liberia" ,"Libya" ,"Liechtenstein" ,"Lithuania" ,"Luxembourg" ,"Madagascar" ,"Malawi" ,"Malaysia" ,"Maldives" ,"Mali" ,"Malta", "Marshall Islands" ,"Martinique" ,"Mauritania" ,"Mauritius", "Mayotte" ,"Mexico" ,"Micronesia (Fed. States of)", "Mongolia" ,"Montenegro" ,"Montserrat", "Morocco","Mozambique" ,"Myanmar" ,"Namibia" ,"Nauru", "Nepal" ,"Netherlands" ,"New Caledonia","New Zealand" ,"Nicaragua" ,"Niger","Nigeria","Niue" ,"North Macedonia" ,"Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines","Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of Moldova", "Reunion", "Romania", "Russian Federation", "Rwanda", "Samoa", "Sao Tome and Principe", "Saudi Arabia","Senegal", "Serbia", "Serbia and Montenegro", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan","Spain", "Sri Lanka", "St. Helena and Depend.", "St. Kitts-Nevis", "St. Lucia", "St. Pierre-Miquelon", "St. Vincent-Grenadines", "State of Palestine", "Sudan", "Suriname","Sweden", "Switzerland", "Syrian Arab Republic", "Tajikistan", "Thailand", "Timor-Leste", "Togo" ,"Tonga", "Trinidad and Tobago", "Tunisia" ,"Turkey", "Turkmenistan","Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United Rep. of Tanzania", "United States", "Uruguay","Uzbekistan","Vanuatu","Venezuela (Bolivar. Rep.)", "Viet Nam","Wallis and Futuna Is.", "Yemen", "Zambia","Zimbabwe"];
var countries2 =["Australia","Austria","Belarus","Belgium","Bulgaria","Canada","Croatia","Cyprus","Czechia","Denmark","Estonia","European Union (Convention)","European Union (KP)","Finland","France","Germany","Greece","Hungary","Iceland","Ireland","Italy","Japan","Kazakhstan","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Monaco","Netherlands","New Zealand","Norway","Poland","Portugal","Romania","Russian Federation","Slovakia","Slovenia","Spain","Sweden","Switzerland","Türkiye","Ukraine","United Kingdom of Great Britain and Northern Ireland","United States of America",]
var countries3 =["Albania","Algeria","Andorra","Argentina","Australia","Austria","Bahrain","Bangladesh","Belarus","Belgium","Bermuda","Bhutan","Botswana","Brazil","British Virgin Islands","Bulgaria","Cameroon","China, Hong Kong Special Administrative Region","China, Macao Special Administrative Region","Colombia","Croatia","Cuba","Curaçao","Cyprus","Czechia","Denmark","Ecuador","Egypt","Estonia","Finland","France","French Polynesia","Germany","Ghana","Guadeloupe","Hungary","Iceland","Ireland","Italy","Japan","Kazakhstan","Kuwait","Latvia","Lebanon","Lithuania","Luxembourg","Malaysia","Malta","Marshall Islands","Martinique","Mauritius","Mexico","Morocco","Nepal","Netherlands","Niger","Norway","Peru","Poland","Portugal","Qatar","Republic of Korea","Réunion","Romania","Saint Vincent and the Grenadines","Samoa","Serbia","Singapore","Slovakia","Slovenia","Spain","State of Palestine","Suriname","Sweden","Switzerland","Thailand","Togo","Tunisia","Turkey","Ukraine","United Arab Emirates","United Kingdom of Great Britain and Northern Ireland","United Republic of Tanzania","United States of America","Zimbabwe",]
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
              b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/

  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}