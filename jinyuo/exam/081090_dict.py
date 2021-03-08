# https://wikidocs.net/22000

print("081")
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, unvalid1, unvalid2 = scores
print(valid_score)

print("\n082")
_, _, *valid_score = scores
print(valid_score)

print("\n083")
_, *valid_score, _ = scores
print(valid_score)

print("\n084")
temp = {}
print(temp)

print("\n085")
temp = {'메로나' : 1000, "플라포" : 1200, "빵빠레" : 1800}
print(temp)

print("\n086")
temp["죠스바"] = 1200
temp["월드콘"] = 1500
print(temp)

print("\n087")
print(f"메로나 가격: {temp['메로나']}")

print("\n088")
temp['메로나'] = 1300
print(temp)

print("\n089")
del temp['메로나']
print(temp)

print("\n090")
temp['누가바']
# dictionary에 키가 없음