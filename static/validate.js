function validate() {
    let data =  JSON.parse(document.getElementById("everyEmployee").content);
    let input = document.addEmployeeForm.id.value;

    for(i = 0; i < data.length; i++) {
        if (input == data[i].employee_number) {
            alert("Id already exist, please choose a new one");
            return false;
        }
    }
    return true;
}