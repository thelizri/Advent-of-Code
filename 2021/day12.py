def decrement(map):
    map1 = dict()
    for k, v in map.items():
        if k == 0:
            map1.update({6 : v})
        else:
            map1.update({k-1 : v})
    return map1 
print({2: 45, 3: 49, 1: 107, 4: 49, 0: 50})
map1 = decrement({2: 45, 3: 49, 1: 107, 4: 49, 0: 50})
print(map1)