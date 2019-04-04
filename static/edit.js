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
    if (date !== null)
        dateField.setAttribute("value", date);
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

    confirmButton.addEventListener("click", function () {
        let sendString = "";
        for (let i = 0; i < row.length - 2; i++) {
            sendString += "#" + row[i].children[0].value;
        }
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
        };
        xhttp.open("POST", "/employee/update", true);
        xhttp.send(sendString);

        setRowToText(id, row, url);
    });


    row[row.length - 2].appendChild(confirmButton);

}

/*
Set each cell to text based on current values when updating
@params id of row, row, url to update
 */
function setRowToText(id, row, url) {
    for (let i = 0; i < row.length - 2; i++) {
        row[i].innerHTML = row[i].children[0].value;
    }
    let button = createButton("Edit");
    button.setAttribute("class", "edit btn btn-secondary");
    button.addEventListener("click", function () {
        editRow(id, url)
    });

    row[row.length - 2].innerHTML = "";
    row[row.length - 2].appendChild(button);
}