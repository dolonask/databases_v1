
def remove_data(lists, delete_data):
    for item in delete_data:
        if item in lists:
            lists.remove(item)
    return lists



