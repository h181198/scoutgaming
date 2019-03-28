function editRow(id, url) {

    let row = document.getElementById(id).cells;

    for (let i = 0; i < row.length - 2; i++) {

        let value = row[i].innerHTML;
        value = value.split(' ').join('');

        if (value.match('None') != null) {
            row[i].innerHTML = '<input class="fool" type="date">';
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
