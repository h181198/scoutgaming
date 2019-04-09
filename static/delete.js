function deleteRow(id, url) {
    if (confirm("Sure you want to delete: " + id + "?")) {
        console.log("DELETED");

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