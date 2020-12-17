# https://wikidocs.net/7021 풀이
#

print("011")
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
# 한글 이름의 변수 사용 가능... 충격적

print("\n012")
시가총액 = 2980000000000
현재가 = 50000
PER = 15.79
print("시가총액 : ", 시가총액)
print("현재가 : ", 현재가)
print("PER : ", PER)

print("\n013")
s = "hello"
t = "python"
print(s, t, sep="! ")
# print(s+"!", t)

print("\n014")
print(2 + 2 * 3)
# 8

print("\n015")
a = "132"
print(type(a))
# <class 'str'>

print("\n016")
num_str = "720"
print(int(num_str), type(int(num_str)))

print("\n017")
num = 100
print(str(num), type(str(num)))

print("\n018")
float_str = "15.79"
print(float(float_str), type(float(float_str)))

print("\n019")
year = "2020"
for x in range(int(year)):
    if x >= int(year)-3:
        print(x)
# print(int(year)-3)  # 2017
# print(int(year)-2)  # 2018
# print(int(year)-1)  # 2019

print("\n020")
per_month = 48584
num_month = 36
total_price = per_month * num_month
print(total_price)
