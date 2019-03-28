 function addEquipment() {

document.getElementById("addButton").disabled = true;

var table = document.getElementById("table");

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


          let cancelButton = document.createElement("INPUT");
        cancelButton.setAttribute("type", "submit");
        cancelButton.setAttribute("value", "Cancel");
        cancelButton.setAttribute("class", "btn btn-danger");
         row.insertCell(7).appendChild(cancelButton);

         cancelButton.addEventListener("click", function () {
         table.deleteRow(-1);
         document.getElementById("addButton").disabled=false;

         });



 }