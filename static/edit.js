/*
Create a button
@param text for button
 */
function createButton(text) {
    let button = document.createElement("button");
    button.innerText = text;
    return button;
}

/*
Create a Date Field
@param date as YYYY-MM-DD
 */
function createDateField(date = null) {
    let dateField = document.createElement("input");
    dateField.setAttribute("type", "date");
    if (date !== null) {
        dateField.setAttribute("value", date);
    }
    return dateField;
}

/*
Create a dropdown menu, you should be able to find the data as an json file in a meta-tag in html
@param type of dropdown, current value
 */
function createDropdown(dropdownType, currentValue) {

    let dropdownData = document.getElementById(dropdownType).content;
    let myObject = JSON.parse(dropdownData);
    let dropdownFiled = document.createElement("select");

    myObject.forEach(result => {
            let option = document.createElement("option");
            option.value = result.id;
            option.text = result.unit;
            dropdownFiled.appendChild(option);
        }
    );

    for (let j = 0; j < dropdownFiled.options.length; j++) {
        if (dropdownFiled.options[j].text === currentValue) {
            dropdownFiled.selectedIndex = j;
            break;
        }
    }
    return dropdownFiled;
}

/*
Create a text field
@param text
 */
function createTextField(text) {
    let textField = document.createElement("input");
    textField.setAttribute("placeholder", text);
    textField.setAttribute("value", text);
    return textField;
}

/*
This function will replace all input in selected row and display editable fields witch the user can change the content
@param id and url
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
    });


    row[row.length - 2].appendChild(confirmButton);
}

/*
Set each cell to text based on current values when updating
@params id of row, row, url to update, json with row text
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

/*
This function will update the update div
 */
function updateStatus(status) {
    let statusDiv = document.getElementById('status');
    let element = document.createElement("div");
    if (status === "update") {
        element.setAttribute('class', "alert alert-success alert-dismissible fade show");
        element.setAttribute('role', 'alert');
        element.innerText = "Table updated";

        let button = document.createElement('button');
        button.setAttribute('type', 'button');
        button.setAttribute('class', 'close');
        button.setAttribute('data-dismiss', 'alert');
        button.setAttribute('aria-label', 'Close');
        button.innerHTML = '<span aria-hidden="true">&times;</span>';

        button.addEventListener('click',function () {
            statusDiv.innerHTML = "";
        });

        element.appendChild(button);
    }
    statusDiv.appendChild(element);
}