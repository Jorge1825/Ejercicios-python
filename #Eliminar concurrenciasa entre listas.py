# Eliminar concurrenciasa entre  listas

test_list = [1, 3, 4, 6, 6, 7]

remove_list = [3, 6]


#res = [i for i in test_list if i not in remove_list]

res = []

for i in test_list:
    if i not in remove_list:
        res.append(i)

print(res)
