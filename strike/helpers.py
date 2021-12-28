import re
import datetime
from main.service import unpucking



def get_request_data(request_data):
    dicts = {}
    for i in request_data:
        dicts.update({
            i['id']: i['item']
        })
    return dicts


def return_right_data(custom_dict_data):
    regex = r'\d{4}-\d{2}-\d{2}'
    new_json = {}
    item = []
    for i, val in custom_dict_data.items():
        for value in val:
            if (re.match(regex, value['id'])):
                item.append(value['id'])
                continue
            item.append(int(value['id']))
        new_json.update({
            i: item
     })
        item = list()
    print(item)
    return new_json


def get_values(data):
    values_list = ['country']
    for i in data.keys():
        print(i)
        if i == "start_date" or i == "end_date":
            continue

        if i == "added_by" or i == "user":
            values_list.append(i + "__username")
            values_list.append(i + "_id")
            continue
        if i == "tradeunion_data":
            values_list.append(i + "__tradeUnion_name")
            values_list.append(i + "_id")
            continue

        if i == "employear":
            values_list.append(i + "__emp_name")
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
        if i == "card_sources" or i == "economic_demands" or  i == "politic_demands" or  i == "combo_demands" or i == "intruder" or i == "source" or i == "violated_right":
            values_list.append(i + "__name")
            values_list.append(i + "__id")

            continue

        if i == "card_demand_categories":
            values_list.append(i + "__demand_cat_name")
            values_list.append(i + "__id")

        else:
            values_list.append(i + "__name")
            values_list.append(i + "_id")

    return values_list


def relativedelta(years):
    pass


def get_data(data):
    """
    Добавляет __in к ключам two
    """
    dicts = {}
    date_st = data.get('start_date', None)
    end_date = data.get('end_date', None)
    print(date_st)
    q = "date_create" + "__range"

    if "start_date" in list(data.keys()) and "end_date" in list(data.keys()):
        datee = date_st + end_date
        dicts.update({q: datee})
        data.pop('start_date')
        data.pop('end_date')

    elif "start_date" in list(data.keys()):
        date_st.append(datetime.datetime.now().date())
        dicts.update({q: (date_st)})
        data.pop('start_date')
    elif "end_date" in list(data.keys()):
        end_date.insert(0, '2000-01-01')
        print(end_date)
        dicts.update({q: end_date})
        data.pop('end_date')
    for i, y in data.items():
        q = i + "__in"
        dicts.update({q: y})
        print(dicts)

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
    # print(lists)
    return lists