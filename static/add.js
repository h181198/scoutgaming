function add(url) {

    document.getElementById("addButton").disabled = true;
    let table = document.getElementById("addTable");
    let row = table.insertRow();
    let addDiv = document.getElementById("addDiv");
    addDiv.style.visibility = 'visible';


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
                console.log(typeof newId);
                location.reload();
                updateStatus("add");
            } else if (request.status === 404) {
                updateStatus()
            }
        };
        request.open("POST", url, true);
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
        row.parentNode.removeChild(row);
        addDiv.style.visibility = 'hidden';
    });
    row.insertCell(table.rows[0].cells.length - 1).appendChild(cancelButton);

}

