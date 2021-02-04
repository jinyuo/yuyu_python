# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:23:13 2021

@author: you
"""

# 111 분기문
"""
string = input("입력:")
print(string * 2)
"""

# 112 분기문
"""
string = input("숫자를 입력하세요:")
print(int(string) + 10)
"""

# 113 분기문
"""
string = input("숫자를 입력하세요:")
if int(string)%2==0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
"""

# 114 분기문
"""
string = input("숫자를 입력하세요:")
if int(string)+20>255 :
    print(255)
else :
    print(int(string)+20)
"""

# 116 분기문
"""
string = input("시간을 입력하세요:")
if string[-2:] == "00" :
    print("정각입니다.")
else :
    print("정각이 아닙니다.")
"""

# 117 분기문
"""
fruit = ["사과","포도","홍시"]
string = input("좋아하는 과일은?:")
if string in fruit :
    print("정답입니다.")
else :
    print("오답입니다.")
"""

# 119 분기문
"""
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
string = input("제가 좋아하는 계절은?:")
if string in fruit :
    print("정답입니다.")
else :
    print("오답입니다.")
"""

# 120 분기문
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
string = input("제가 좋아하는 과일은?:")
if string in fruit.values() :
    print("정답입니다.")
else :
    print("오답입니다.")
