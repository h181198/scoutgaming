# input data must be string, send it in as str(data)
def create_data(data):
    return data[2:len(data)-1].split('#')[1:]