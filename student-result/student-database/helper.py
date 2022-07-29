
def search(name):
    data = mycollection.find_one({"name": name})

    if data:
        return data
    else:
        return None



def display_messages(t, message):
    if t == 's':
        info = "operation was successful. "+ message

    else:
        info = "operation not successful. " + message

    return info