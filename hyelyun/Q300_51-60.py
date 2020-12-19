# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:10:36 2020

@author: you
"""

# 051 리스트
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 052 리스트
movie_rank.append("배트맨")
print(movie_rank)

# 053 리스트
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054 리스트
#movie_rank.remove("럭키")
del movie_rank[3]
print(movie_rank)

# 055 리스트
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
'''
del을 이용하여 리스트에서 원소 삭제 가능
단, 리스트에서 어떤 값을 삭제하면 남은 값들이 새로 인덱싱 됨
'''

# 056 리스트
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057 리스트
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))
print(max(nums))

# 058 리스트
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 059 리스트
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060 리스트
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))