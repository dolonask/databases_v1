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
     }
        )
        item = list()
    return new_json

