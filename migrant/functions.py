def unpucking(list):
    res = ', '.join(list)
    return res

def filter_objects(*args):
    list1 = []
    for i in args:
        for j in i:
            a = f"{j}={j}"
            list1.append(a)

    print(list1)
    return list1

arg = {'country': ['1'], 'region': ['2']}

lists = filter_objects(arg)
print(unpucking(lists))

