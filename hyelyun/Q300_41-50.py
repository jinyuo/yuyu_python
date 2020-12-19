# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:39:39 2020

@author: you
"""

# 041 문자열
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

# 042 문자열
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)

# 043 문자열
a = "hello"
a = a.capitalize()
print(a)

# 044 문자열
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
print(file_name.endswith("xlsx"))
'''
endswith : 끝 문자 확인
'''
# 045 문자열
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 046 문자열
a = "hello world"
print(a.split())

# 048 문자열
ticker = "btw_krw"
print(ticker.split("_"))

# 050 문자열
data = "039490     "
print(data.rstrip())
