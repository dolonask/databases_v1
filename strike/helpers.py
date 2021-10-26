
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
        print(i)
        if i == "added_by" or i == "user":
            values_list.append(i + "__username")
            values_list.append(i + "_id")
            continue
        if i == "tradeunion_data":
            values_list.append(i + "__tradeUnion_name")
            values_list.append(i + "_id")
            continue


        if i == "count_strike_participants":
            values_list.append(i + "__choice")
            values_list.append(i + "_id")
            continue

        if i == "company_employees_count":
            values_list.append(i + "__choice")
            values_list.append(i + "_id")
            continue
        if i == "card_sources" or i == "economic_demands" or  i == "politic_demands" or  i == "combo_demands" or i == "intruder" or i == "source":
            values_list.append(i + "__name")
            continue

        if i == "card_demand_categories":
            values_list.append(i + "__demand_cat_name")
            # values_list.append(i + "_id")

        else:
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
    print(lists)
    return lists