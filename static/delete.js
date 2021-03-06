/**
 * Delete row from database if confirmed by user
 * @param id
 * @param url
 */
function deleteRow(id, url) {
    if (confirm("Are you sure you want to delete this row?")) {

        let request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
                table.row('#'+ id+'').remove().draw();
                updateStatus("delete");
            } else if (request.status === 404) {
                updateStatus()
            }
        };
        request.open("POST", url, true);
        request.send(id);
    }

}

