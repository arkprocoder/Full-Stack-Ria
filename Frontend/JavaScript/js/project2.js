//  constructor
console.log("Welcome to my project -2 using es6 version ");
class Covid {
  constructor(name, email, adhar, type) {
    this.name = name;
    this.email = email;
    this.adhar = adhar;
    this.type = type;
  }
}

class Display {
  add(covid) {
    let tablebody;
    tablebody = document.getElementById("tableBody");
    let uistring = `<tr>
                
    <td>${covid.name}</td>
    <td>${covid.email}</td>
    <td>${covid.adhar}</td>
    <td>${covid.type}</td>
  </tr>`;
    tablebody.innerHTML += uistring;
  }
  clear() {
    let covidForm = document.getElementById("covidform");
    covidForm.reset();
  }

  validate(covid) {
    console.log("Validating");
    if (
      covid.name.length < 2 ||
      covid.email.length < 5 ||
      covid.adhar.length < 2
    ) {
      return false;
    } else {
      return true;
    }
  }

  show(type, displayMessage) {
    let message = document.getElementById("showmessage");
    message.innerHTML = `<div class="alert alert-${type}" role="alert">
    ${displayMessage}
  </div>`;
    setTimeout(function () {
      message.innerHTML = "";
    }, 2000);
  }
}
// add submit event listener to the covid form
let covidForm = document.getElementById("covidform");
covidForm.addEventListener("submit", covidFormSubmit);

function covidFormSubmit(e) {
  console.log("your submitting the covid form");
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let adhar = document.getElementById("adhar").value;
  let gmale = document.getElementById("male");
  let gfemale = document.getElementById("female");
  console.log(name, email, adhar, gmale, gfemale);
  let type;
  if (gmale.checked) {
    type = gmale.value;
  } else if (gfemale.checked) {
    type = gfemale.value;
  }
  e.preventDefault();

  let covid = new Covid(name, email, adhar, type);
  console.log(covid);
  let display = new Display();

  if (display.validate(covid)) {
    console.log("perfect now you can add the data");
    display.add(covid);
    display.clear();
    display.show("success", "Registration Success");
  } else {
    display.show("danger", "Registration Fails");
    display.clear();
  }
}