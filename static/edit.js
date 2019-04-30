/**
 * This function will replace all input in selected row and display editable fields witch the user can change the content
 * @param id
 * @param url
 */
let stack = [true];

function editRow(id, url, deleteUrl) {
    $('td').attr("data-toggle", "");

    /*
    We create a stack. so we know how many elements we are editing at a given time.
     */
    stack.push(false);

    let table = document.getElementById("table");
    let row = document.getElementById(id).cells;

    for (let i = 0; i < row.length - 2; i++) {
        let value = row[i].innerHTML;
        value = value.split('  ').join('').split('\n').join('');

        if (table.rows[0].cells[i].classList.contains("ignore")) {

        } else if (table.rows[0].cells[i].classList.contains("department")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDropdown("department", "departmentData", value));
        } else if (table.rows[0].cells[i].classList.contains("equipment")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDropdown("equipment", "equipmentData", value));
        } else if (table.rows[0].cells[i].classList.contains("receipt")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDropdown("receipt", "receiptData", value));
        } else if (table.rows[0].cells[i].classList.contains("employee")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDropdown("employee", "employeeData", value));
        } else if (table.rows[0].cells[i].classList.contains("date")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDateField(value));
        } else {
            row[i].innerHTML = "";
            row[i].appendChild(createTextField(value))
        }
    }


    /*
    Create confirm button and add functionality
     */
    row[row.length - 2].innerHTML = '';
    let confirmButton = createButton("Confirm");
    confirmButton.setAttribute("class", "btn btn-info");

    function createDeleteButton() {
        let deleteButton = createButton("Delete");
        deleteButton.setAttribute("class", "btn btn-danger");
        deleteButton.addEventListener("click", function () {
            deleteRow(id, deleteUrl);
        });
        return deleteButton;
    }


    /*
    This is what happens when you click the confirm button
     */
    confirmButton.addEventListener("click", function () {
        let sendString = "#" + id;
        for (let i = 0; i < row.length - 2; i++) {
            if (!table.rows[0].cells[i].classList.contains("ignore")) {
                sendString += "#" + row[i].children[0].value;
            }
        }


        /*
        We use ajax to connect with the server since we do not want to reload the page, this method will return a json on callback
         */
        let request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
                setRowToText(id, row, url, deleteUrl, JSON.parse(request.responseText));
                updateStatus("update");
                stack.pop();
                if (stack[stack.length - 1]) {
                    $('td').attr("data-toggle", "modal");
                }

                let deleteButton = createDeleteButton();
                row[row.length - 1].innerHTML = '';
                row[row.length - 1].appendChild(deleteButton);
            } else if (request.status === 404) {
                updateStatus()
            }

        };
        request.open("POST", url, true);
        request.send(sendString);
    });
    row[row.length - 2].appendChild(confirmButton);

    /*
Create a cancel button
 */
    let cancelButton = createButton("Cancel");
    cancelButton.setAttribute("class", "btn btn-danger");

    let defaultValues = [];
    for (let i = 0; i < row.length - 2; i++) {
        if (table.rows[0].cells[i].classList.contains("ignore")) {
            defaultValues[i] = null;
        } else if (table.rows[0].cells[i].classList.contains("department")) {
            defaultValues[i] = createNormalText("department", "departmentData", row[i].children[0].value);
        } else if (table.rows[0].cells[i].classList.contains("equipment")) {
            defaultValues[i] = createNormalText("equipment", "equipmentData", row[i].children[0].value);
        } else if (table.rows[0].cells[i].classList.contains("employee")) {
            defaultValues[i] = createNormalText("employee", "employeeData", row[i].children[0].value);
        } else if (table.rows[0].cells[i].classList.contains("receipt")) {
            defaultValues[i] = createNormalText("receipt", "receiptData", row[i].children[0].value);
        } else {
            defaultValues[i] = row[i].children[0].value;
        }
    }

    cancelButton.addEventListener("click", function () {
        stack.pop();
        if (stack[stack.length - 1]) {
            $('td').attr("data-toggle", "modal");
        }
        for (let i = 0; i < row.length - 2; i++) {
            if (defaultValues[i] !== null) {
                if (defaultValues[i] !== "")
                    row[i].innerHTML = defaultValues[i];
                else
                    row[i].innerHTML = "None";
            }
        }

        let deleteButton = createDeleteButton();
        let editButton = createButton("Edit");
        editButton.setAttribute("class", "edit btn btn-secondary");
        editButton.addEventListener("click", function () {
            editRow(id, url, deleteUrl);
        });
        row[row.length - 2].innerHTML = '';
        row[row.length - 2].appendChild(editButton);

        row[row.length - 1].innerHTML = '';
        row[row.length - 1].appendChild(deleteButton);

    });
    row[row.length - 1].innerHTML = '';
    row[row.length - 1].appendChild(cancelButton);

}
