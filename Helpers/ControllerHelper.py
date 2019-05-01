from Services.EquipmentService import EquipmentService as EqS
from Services.EmployeeService import EmployeeService as EmS
from Services.TransactionService import TransactionService as TrS
import re


# input data must be string, send it in as str(data)
def create_data(data):
    return data.split('#')[1:]


def create_single_id(data):
    return data[2:len(data)-1].split('\'')


def string_to_list(session, data):
    data = data[1:len(data) - 1]
    data = data.split('>, ')
    results = []

    if data[0][1:6] == "Equip":
        for item in data:
            identity = int(re.search('id=\'(.*)\', m', item).group(1))
            results.append(EqS.find_equipment(session, identity))
    elif data[0][1:6] == "Emplo":
        for item in data:
            identity = int(re.search('id=\'(.*)\', empl', item).group(1))
            results.append(EmS.find_employee(session, identity))
    elif data[0][1:6] == "Trans":
        for item in data:
            identity = int(re.search('id=\'(.*)\', empl', item).group(1))
            results.append(TrS.find_transaction(session, identity))

    return results


def secure_text(input_text):
    return input_text.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;")
