# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:10:18 2021

@author: you
"""

# 081 리스트 
socres = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_socre, _, _= socres # star expression
print(valid_socre)

# 082 리스트
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

# 083 리스트
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)
print(type(valid_score))

# 084 딕셔너리
temp = {}
print(type(temp))

# 085 딕셔너리
temp = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(temp)
print(type(temp))

# 086 딕셔너리
temp["죠스바"] = 1200
temp["월드콘"] = 1500
print(temp)

# 087 딕셔너리
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격: ",ice["메로나"])

# 088 딕셔너리
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice["메로나"] = 1300;
print(ice["메로나"])

# 089 딕셔너리
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice["메로나"]
print(ice)

# 090 딕셔너리
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#icecream["누가바"]
