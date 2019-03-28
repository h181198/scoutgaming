function editRow(id, url) {

    let table = document.getElementById("table");

    let row = document.getElementById(id).cells;

    for (let i = 0; i < row.length - 2; i++) {

        let value = row[i].innerHTML;
        value = value.split(' ').join('');

        if (value.match('None') != null) {
            row[i].innerHTML = '<input class="fool" type="date">';
        } else if (table.rows[0].cells[i].classList.contains("department")) {

            let dat = document.getElementById("departmentData").content;
            let myObject = JSON.parse(dat);

            let selectList = document.createElement("select");
            selectList.id = "departmentSelect";
            let vv = row[i].innerHTML;
            vv = vv.split(' ').join('');
            vv = vv.split('\n').join('');
            row[i].innerHTML = "";
            row[i].appendChild(selectList);
            myObject.forEach(result => {
                    let option = document.createElement("option");
                    option.value = result.id;
                    option.text = result.unit;
                    selectList.appendChild(option);
                }
            );
            for (let j = 0; j <  selectList.options.length; j++) {
                if (selectList.options[j].text === vv) {
                    selectList.selectedIndex = j;
                    break;
                }
            }
            selectList.setAttribute('class', 'fool');
        } else if (value.match('([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))')) {
            value = value.split('\n').join('');
            row[i].innerHTML = '<input class="fool" type="date" value="' + value + '" >';
        } else {
            row[i].innerHTML = '<input class="fool" type="text" size="8" value="' + value + '">';
        }
    }


    row[row.length - 2].innerHTML = '';
    let confirmButton = document.createElement("INPUT");
    confirmButton.setAttribute("type", "submit");
    confirmButton.setAttribute("value", "Confirm");
    confirmButton.setAttribute("class", "btn btn-info");


    confirmButton.addEventListener("click", function () {
        let valueList = document.getElementsByClassName('fool');
        let valueString = "";

        for (let i = 0; i < valueList.length; i++) {
            if (!(valueList[i].value.localeCompare(""))) {
                valueString += "/None"
            } else {
                valueString += "/" + valueList[i].value;

            }
        }
        location.replace(url + valueString);
    });

    row[row.length - 2].appendChild(confirmButton);

}
