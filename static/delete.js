/*
Delete row from database if confirmed by user
@param id, url
 */
function deleteRow(id, url) {
    if (confirm("Are you sure you want to delete this row?")) {

        let request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
                let row = document.getElementById(id);
                row.parentNode.removeChild(row);
                updateStatus("delete");
            }
        };
        request.open("POST", url, true);
        request.send(id);
    }

}