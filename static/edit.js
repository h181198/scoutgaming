
/**
 * This function will replace all input in selected row and display editable fields witch the user can change the content
 * @param id
 * @param url
 */
function editRow(id, url) {
    let table = document.getElementById("table");
    let row = document.getElementById(id).cells;

    for (let i = 0; i < row.length - 2; i++) {
        let value = row[i].innerHTML;
        value = value.split(' ').join('').split('\n').join('');

        if (value.match('None') != null) {
            row[i].innerHTML = "";
            row[i].appendChild(createDateField());
        } else if (table.rows[0].cells[i].classList.contains("department")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDropdown("departmentData", value));
        } else if (value.match('([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))')) {
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

    row[row.length - 2].appendChild(confirmButton);

    /*
    This is what happens when you click the confirm button
     */
    confirmButton.addEventListener("click", function () {
        let sendString = "#" + id;
        for (let i = 0; i < row.length - 2; i++) {
            sendString += "#" + row[i].children[0].value;
        }
        /*
        We use ajax to connect with the server since we do not want to reload the page, this method will return a json on callback
         */
        let request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
                setRowToText(id, row, url, JSON.parse(request.responseText));
                updateStatus("update");
            }
        };
        request.open("POST", "/employee/update", true);
        request.send(sendString);
        console.log(sendString)
    });


    row[row.length - 2].appendChild(confirmButton);
}

/**
 * Set each cell to text based on current values when updating
 * @param id
 * @param row
 * @param url
 * @param json
 */
function setRowToText(id, row, url, json) {
    let array = [];
    for (let key in json) {
        if (json[key] === null) {
            array.push("None")
        } else {
            array.push(json[key]);
        }
    }

    for (let i = 1; i < array.length; i++) {
        row[i - 1].innerHTML = array[i];
    }

    let button = createButton("Edit");
    button.setAttribute("class", "edit btn btn-secondary");
    button.addEventListener("click", function () {
        editRow(id, url)
    });

    row[row.length - 2].innerHTML = "";
    row[row.length - 2].appendChild(button);
}
