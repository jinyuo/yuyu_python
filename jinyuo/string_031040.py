# https://wikidocs.net/7024
# 문자열 formatting 방법 정리할 것

print("031")
a = "3"
b = "4"
print(a + b)
# 34

print("\n032")
print("Hi" * 3)
# HiHiHi

print("\n033")
print("-" * 80)

print("\n034")
t1 = 'python'
t2 = 'java'
t = t1 + " " + t2
print(t * 4)

print("\n035")
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2))

print("\n036")
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

print("\n037")
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

print("\n038")
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))
print (f"상장주식수 : {상장주식수} type : {type(상장주식수)}")

print("\n039")
분기 = "2020/03(E) (IFRS연결)"
print(분기.split("(")[0])

print("\n040")
data = "   삼성전자   "
print(data.strip())
