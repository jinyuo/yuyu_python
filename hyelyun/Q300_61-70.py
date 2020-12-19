# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:38:56 2020

@author: you
"""

# 061 리스트
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062 리스트
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 063 리스트
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 064 리스트
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065 리스트
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 066 리스트
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

'''
join 메서드 : 리스트를 문자열로 붙일 때 사용
'''

# 067 리스트
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 068 리스트
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 069 리스트
string = "삼성전자/LG전자/Naver"
strlist = string.split("/")
print(strlist)

# 070 리스트
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
'''
print(data.sort()) : None 으로 출력됨. 정렬만 하고 결과값은 없는듯
'''

data2 = [2, 4, 3, 1, 5, 10, 9]
data3 = sorted(data)
print(data3)
'''
sorted 메서드 사용
'''