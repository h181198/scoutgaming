function add() {
  document.getElementById("addButton").disabled = true;
  var table = document.getElementById("table");
  var row = table.insertRow(-1);

  for (let i = 0; i < table.rows[0].cells.length-2; i++) {
    var x = document.createElement("INPUT");

    if (table.rows[0].cells[i].classList.contains("date")) {
      x.setAttribute("type", "date");
    } else {
      x.setAttribute("type", "text");
    }

    x.setAttribute("size", 8);
    cell = row.insertCell(i);
    cell.appendChild(x);
  }

  confirmButton = createConfirmButton();
  row.insertCell(table.rows[0].cells.length-2).appendChild(confirmButton);

  cancelButton = createCancelButton();
  row.insertCell(table.rows[0].cells.length-1).appendChild(cancelButton);
}

function createCancelButton() {
  let cancelButton = document.createElement("INPUT");
  cancelButton.setAttribute("type", "submit");
  cancelButton.setAttribute("value", "Cancel");
  cancelButton.setAttribute("class", "btn btn-danger");
  cancelButton.addEventListener("click", function() {
    table.deleteRow(-1);
    document.getElementById("addButton").disabled = false;
  });
  return cancelButton;
}

function createConfirmButton() {
  let confirmButton = document.createElement("INPUT");
  confirmButton.setAttribute("type", "submit");
  confirmButton.setAttribute("value", "Confirm");
  confirmButton.setAttribute("class", "btn btn-info");
  return confirmButton;
}
