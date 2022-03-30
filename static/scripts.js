function checkTextField() {
    var option = document.getElementById('contact').value;
    var textbox = document.getElementById('textbox')
    var carrier = document.getElementById('carrier')
    console.log(option)

    if (option == "phone") {
        carrier.innerHTML="<input type='text' id='input_carrier' placeholder='carrier' name='input_carrier'>";
        textbox.innerHTML="<input type='text' id='input' placeholder='phone number' name='input'>";
        return;
    }

    if (option == "email") {
        toAppend = "<input type='text' id='input' placeholder='email' name='input'>";
        textbox.innerHTML=toAppend;
        return;
    }
}

function validity() {
  var value = document.getElementById('contact');
  var tb = document.getElementById('input');

  if (value == "phone") {

    var phoneno = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;

    if (tb.value.match(phoneno)) {
      return true;
    }

    else {
      alert("Phone number invalid")
      return false;
    }
  }

  if (value == "email") {
    var email_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (tb.value.match(email_regex)) {
      return true;
    }

    else {
      alert("Email invalid")
      return false;
    }
  }
}

function check_carrier() {
  carrier = document.getElementById("input_carrier").value
  if (carrier == "tmobile" || carrier == "verizon" || carrier == "sprint" || carrier == "at&t") {
    return true;
  }

  else {
    alert("Carrier invalid");
    return false;
  }
}

function check_input() {
  var contact = document.getElementById('input').value;
  var carrier = document.getElementById('input_carrier').value;
  var selection = document.getElementsByName("dropdown");
  var checked = 0;

  if (contact == "") {
    alert("Enter contact");
    return false;
  }

  if (carrier == "" && contact == "phone") {
    alert("Must enter carrier");
    return false;
  }

  if (carrier != "tmobile" && carrier != "sprint" && carrier != "verizon" && carrier != "at&t") {
    alert("Invalid carrier");
    return false;
  }

  for (var value of selection.values()) {
    if (value.checked == true) {
      checked += 1;
    }
  }
  console.log(checked);

  if (checked == 0) {
    alert("Select options");
    return false;
  }
  else {
    return true;
  }
}
