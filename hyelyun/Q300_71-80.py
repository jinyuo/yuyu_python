# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:05:12 2021

@author: you
"""

# 071 튜플
my_variable = ()
print(type(my_variable))

# 072 튜플
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 073 튜플
number = (1)
print(number)
print(type(number)) # 튜플이 아닌 정수로 인식
number2 = (1,)
print(type(number2))

# 074 튜플
t = (1,2,3)
#t[0] = 'a' # 튜플은 원소의 값을 변경할 수 없음**

# 075 튜플
t2 = 1,2,3,4
print(type(t2))

# 076 튜플
t3 = ('a', 'b', 'c')
t3 = ('A','b', 'c')
print(t3)

# 077 튜플
interest = ('삼성전자', 'LG전자', 'SK hynix')
data = list(interest)
print(type(data))

# 078 튜플
interest = ['삼성전자', 'LG전자', 'SK hynix']
data = tuple(interest)
print(type(data))

# 079 튜플 언팩킹**
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 튜플
data = tuple(range(2,100,2))
print(data)