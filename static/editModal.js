function updateTableRow(id) {
    console.log(id);
    let row = document.getElementById(id).cells;
    let table = document.getElementById("table");
    let array = [id, document.getElementById("price" + id).value, document.getElementById("currency" + id).value,
        document.getElementById("model" + id).value, document.getElementById("buy-date" + id).value,
        document.getElementById("receipt" + id).value, document.getElementById("description" + id).value,
        document.getElementById("note" + id).value];


    let sendString = "";
    for (let i = 0; i < array.length; i++) {
        sendString += "#" + array[i];
    }
    /*
    We use ajax to connect with the server since we do not want to reload the page, this method will return a json on callback
     */
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {

            for (let i = 0; i < array.length; i++) {
                if (table.rows[0].cells[i].classList.contains("receipt")) {
                    row[i].innerText = createNormalText("receipt", "receiptData",array[i]);
                } else {
                    row[i].innerText = array[i];

                }


            }

            updateStatus("update");
        } else if (request.status === 404) {
            updateStatus()
        }

    };
    request.open("POST", "/equipment/update", true);
    request.send(sendString);

}