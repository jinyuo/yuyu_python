# https://wikidocs.net/78563

print("091")
inventory = {"메로나" : [300 , 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
print(inventory)

print("\n092")
print(f"{inventory['메로나'][0]}원")

print("\n093")
print(f"{inventory['메로나'][1]}원")

print("\n094")
inventory["월드콘"] = [500, 7];
print(inventory)

print("\n095")
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
keyList = icecream.keys();
print(keyList);

print("\n096")
valueList = icecream.values();
print(valueList);

print("\n097")
print(sum(valueList));

print("\n098")
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

print("\n099")
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)


print("\n100")
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)