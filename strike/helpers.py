
def get_request_data(request_data):
    dicts = {}
    for i in request_data:
        dicts.update({
            i['id']: i['item']
        })
    return dicts


def return_right_data(custom_dict_data):
    new_json = {}
    item = []
    for i, val in custom_dict_data.items():
        for value in val:
            item.append(int(value['id']))
        new_json.update({
            i: item
     })
        item = list()
    return new_json


def get_values(data):
    values_list = []
    for i in data.keys():
        values_list.append(i + "__name")
        values_list.append(i + "_id")
    return values_list


def get_data(data):
    """
    Добавляет __in к ключам two
    """
    dicts = {}
    for i, y in data.items():
        q = i + "__in"
        dicts.update({q: y})
    return dicts


def get_fields(data):
    """
    Добавляет _id к ключам two
    """
    lists = []
    for i in data.keys():
        q = i + '_id'
        lists.append(i)
        lists.append(q)
    return lists