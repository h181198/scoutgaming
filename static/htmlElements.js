/**
 * Create a button
 * @param text
 * @returns {HTMLElement}
 */
function createButton(text) {
    let button = document.createElement("button");
    button.innerText = text;
    return button;
}

/**
 * Create a Date Field
 * @param date
 * @returns {HTMLElement}
 */
function createDateField(date = null) {
    let dateField = document.createElement("input");
    dateField.setAttribute("type", "date");
    if (date !== null) {
        dateField.setAttribute("value", date);
    }
    return dateField;
}

/**
 * Create a text field
 * @param text
 * @returns {HTMLElement}
 */
function createTextField(text = null) {
    let textField = document.createElement("input");
    if (text !== null) {
        textField.setAttribute("placeholder", text);
        textField.setAttribute("value", text);
    }
    return textField;
}

/**
 * Create a dropdown menu, you should be able to find the data as an json file in a meta-tag in html
 * @param dropdownType
 * @param currentValue
 * @returns {HTMLElement}
 */
function createDropdown(dropdownType, currentValue = null) {

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
    if (currentValue != null) {
        for (let j = 0; j < dropdownFiled.options.length; j++) {
            if (dropdownFiled.options[j].text === currentValue) {
                dropdownFiled.selectedIndex = j;
                break;
            }
        }
    }

    return dropdownFiled;
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
