 function addEquipment() {
var table = document.getElementById("equipment-table");

var row = table.insertRow(-1);

for(let i = 0; i < 6; i++){

          var x = document.createElement("INPUT");
          x.setAttribute("type", "text");
          x.setAttribute("size", 8)
          cell = row.insertCell(i);
          cell.appendChild(x)




        }
  let confirmButton = document.createElement("INPUT");
        confirmButton.setAttribute("type", "submit");
        confirmButton.setAttribute("value", "Confirm");
        confirmButton.setAttribute("class", "btn btn-info");
         row.insertCell(6).appendChild(confirmButton);


          let deleteButton = document.createElement("INPUT");
        deleteButton.setAttribute("type", "submit");
        deleteButton.setAttribute("value", "Cancel");
        deleteButton.setAttribute("class", "btn btn-danger");
         row.insertCell(7).appendChild(deleteButton);

 }