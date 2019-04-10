/**
 * This function will update the status div
 * @param status
 */
function updateStatus(status) {
    let statusDiv = document.getElementById('status');
    statusDiv.innerHTML = "";
    let element = document.createElement("div");
    //element.setAttribute('role', 'alert');

    /*
    close div button
     */
    let button = document.createElement('button');
    button.setAttribute('type', 'button');
    button.setAttribute('class', 'close');
    button.setAttribute('data-dismiss', 'alert');
    button.setAttribute('aria-label', 'Close');
    button.innerHTML = '<span aria-hidden="true">&times;</span>';
    button.addEventListener('click', function () {
        statusDiv.innerHTML = "";
    });

    if (status === "update") {
        element.innerText = "Table updated";
        element.setAttribute('class', "alert alert-success alert-dismissible  show");
    } else if (status === "delete") {
        element.innerText = "Row deleted";
        element.setAttribute('class', "alert alert-danger alert-dismissible  show");
    } else if(status === "add"){
        element.innerText = "Row added";
        element.setAttribute('class', "alert alert-success alert-dismissible  show");
    }else{
        return;
    }
    element.appendChild(button);
    statusDiv.appendChild(element);
}