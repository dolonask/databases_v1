

def unpucking(list):
    res = ','.join(list)
    return res

def get_params(*args):
    lists = []
    for i in args:
        # print(i)
        for x in i.keys():

            lists.append(f"{x}={x}")
    return lists


a = {'country': ['6'], 'region': ['86']}
# print(type(typea))
c = get_params(a)
print(unpucking(c)[0])
