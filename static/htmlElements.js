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
         textField.setAttribute("maxlength", 100);
    }
    return textField;
}

/**
 * Create a dropdown menu, you should be able to find the data as an json file in a meta-tag in html
 * @param model, which model the dropdown will be created based on
 * @param dropdownType, data to be found in  the meta-tag
 * @param currentValue
 * @returns {HTMLElement}
 */
function createDropdown(model, dropdownType, currentValue = null) {

    let dropdownData = document.getElementById(dropdownType).content;
    let myObject = JSON.parse(dropdownData);
    let dropdownField = document.createElement("select");

    myObject.forEach(result => {
            let option = document.createElement("option");
            option.value = result.id;
            switch (model) {
                case "department":
                    option.text = result.unit;
                    break;
                case "equipment":
                    option.text = "Id: " + result.id + ", " + result.description;
                    break;
                case "receipt":
                    option.text = result.comb_id;
                    break;
                default:
                    option.text = result.name;
                    break;
            }
            dropdownField.appendChild(option);
        }
    );
    if (currentValue != null) {
        for (let j = 0; j < dropdownField.options.length; j++) {
            if (dropdownField.options[j].text === currentValue) {
                dropdownField.selectedIndex = j;
                break;
            }
        }
    }

    return dropdownField;
}

/**
 * Create a string from a dropdown menu. Often used chen canceling a edit.
 * @param model
 * @param dropdownType
 * @param currentValue
 * @returns {string}
 */
function createNormalText(model, dropdownType, currentValue = null) {
    let myString = "None";

    let dropdownData = document.getElementById(dropdownType).content;
    let myObject = JSON.parse(dropdownData);

    myObject.forEach(result => {
            switch (model) {
                case "department":
                    if (parseInt(result.id) === parseInt(currentValue)) {
                        myString = result.unit;
                    }
                    break;
                case "equipment":
                    if (parseInt(result.id) === parseInt(currentValue)) {
                        myString = result.description;
                    }
                    break;
                case "employee":
                    if (parseInt(result.id) === parseInt(currentValue)) {
                        myString = result.name;
                    }
                    break;
                case "receipt":
                    if (parseInt(result.id) === parseInt(currentValue)) {
                        myString = result.comb_id;
                    }
                    break;
                default:
                    myString = "None";
                    break;
            }
        }
    );
    return myString;
}

/**
 * Set each cell to text based on current values when updating
 * @param id
 * @param row
 * @param url
 * @param json
 */
function setRowToText(id, row, url, delurl, json) {
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
        editRow(id, url, delurl)
    });

    row[row.length - 2].innerHTML = "";
    row[row.length - 2].appendChild(button);
}
