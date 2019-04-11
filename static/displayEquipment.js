function employeeEquipmentInfo(empId, empName) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
            let title = document.getElementById('modal-title');
            title.innerText = empName;
            let table = document.getElementById('equTable');
            table.innerHTML = "";

            let row = document.createElement("tr");

            let model = document.createElement("th");
            model.innerText = 'Model';
            row.appendChild(model);

            let description = document.createElement("th");
            description.innerText = "Description";
            row.appendChild(description);

            let note = document.createElement("th");
            note.innerText = "Note";
            row.appendChild(note);
            table.appendChild(row);


            try {
                let equJson = JSON.parse(request.responseText);
                for (let i in equJson) {
                    row = document.createElement("tr");

                    let modelCol = document.createElement("td");
                    modelCol.innerText = equJson[i].model;
                    row.appendChild(modelCol);

                    let descriptionCol = document.createElement("td");
                    descriptionCol.innerText = equJson[i].description;
                    row.appendChild(descriptionCol);

                    let noteCol = document.createElement("td");
                    noteCol.innerText = equJson[i].note;
                    row.appendChild(noteCol);

                    table.appendChild(row)
                }
            } catch (e) {
                console.log("Empty")
            }

        }
    };
    request.open("GET", "/employee/equipment/" + empId, true);
    request.send();
}