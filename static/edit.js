/**
 * This function will replace all input in selected row and display editable fields witch the user can change the content
 * @param id
 * @param url
 */
var stack = [true];
function editRow(id, url) {
    $('tr').attr("data-toggle", "");
    stack.push(false);
    let table = document.getElementById("table");
    let row = document.getElementById(id).cells;

    for (let i = 0; i < row.length - 2; i++) {
        let value = row[i].innerHTML;
        value = value.split('  ').join('').split('\n').join('');

        if (table.rows[0].cells[i].classList.contains("ignore")) {

        } else if (table.rows[0].cells[i].classList.contains("department")) {
            row[i].innerHTML = "";
            row[i].appendChild(createDropdown("departmentData", value));
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

    row[row.length - 2].appendChild(confirmButton);

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
                setRowToText(id, row, url, JSON.parse(request.responseText));
                updateStatus("update");
                stack.pop();
                if (stack[stack.length-1]) {
                    $('tr').attr("data-toggle", "modal");
                }

            } else if (request.status === 404) {
                updateStatus()
            }
        };
        request.open("POST", url, true);
        request.send(sendString);
    });


    row[row.length - 2].appendChild(confirmButton);
}

