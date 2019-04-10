function add() {
    document.getElementById("addButton").disabled = true;
    let table = document.getElementById("table");
    let row = table.insertRow(-1);

    for (let i = 0; i < table.rows[0].cells.length - 2; i++) {
        let element;
        if (table.rows[0].cells[i].classList.contains("date")) {
            element = createDateField()
        } else if (table.rows[0].cells[i].classList.contains("department")) {
            element = createDropdown("departmentData");
        } else {
            element = createTextField()
        }
        let cell = row.insertCell(i);
        cell.appendChild(element);
    }

    /*
        Confirm button
     */
    let confirmButton = createButton("Confirm");
    confirmButton.setAttribute("class", "btn btn-info");
    confirmButton.addEventListener("click", function () {
        console.log(row);
        console.log(table.rows[0].cells.length);
        let sendString = "";

        for (let i = 0; i < table.rows[0].cells.length - 2; i++) {
            sendString += "#" + row.cells[i].children[0].value;
        }

        let request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
                document.getElementById("addButton").disabled = false;
                let newJson = JSON.parse(request.responseText);
                let newId = newJson.id;
                console.log(newId);
                setRowToText();
                updateStatus("add");
            }
        };
        request.open("POST", "/employee/add", true);
        request.send(sendString);
    });
    row.insertCell(table.rows[0].cells.length - 2).appendChild(confirmButton);


    /*
        Cancel button
     */
    let cancelButton = createButton("Cancel");
    cancelButton.setAttribute("class", "btn btn-danger");
    cancelButton.addEventListener("click", function () {
        document.getElementById("addButton").disabled = false;
    });
    row.insertCell(table.rows[0].cells.length - 1).appendChild(cancelButton);

}
