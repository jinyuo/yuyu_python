# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:00:32 2020

@author: you
"""

# 031 문자열
a = "3"
b = "4"
print(a+b)

# 032 문자열
print("Hi"*3)

# 034 문자열
t1 = 'python'
t2 = 'java'
print((t1+" "+t2+" ")*3)

# 035 문자열
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1,age1))
print("이름: %s 나이: %d" %(name2,age2))

# 036 문자열
print("이름: {} 나이: {}".format(name1, age1))
'''
format 메서드 : 타입과 상관없이 출력될 위치에 {} 적으면 됨
'''

# 037 문자열
print(f"이름: {name1} 나이: {age1}")
'''
파이썬 3.6부터 지원하는 f-string
'''

# 038 문자열
상장주식수 = "5,969,782,550"
상장주식수_str = 상장주식수.replace(",","")
print(int(상장주식수_str))

# 039 문자열
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040 문자열
data = "   삼성전자    "
data2 =data.strip()
print(data2)