# https://wikidocs.net/7027

print("071")
my_variable = ()

print("\n072")
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

print("\n073")
num = (1)

print("\n074")
t = (1, 2, 3)
# t[0] = 'a'
# 리스트와 다르게 튜플은 값 변경 불가

print("\n075")
t = 1, 2, 3, 4
print(type(t))
# tuple

print("\n076")
t = ('a', 'b', 'c')
tList = list(t)
tList[0] = 'A'
t = tuple(tList)
print(t)
# list로 형병환 -> 수정 -> tuple로 형변환

print("\n077")
interest = ('삼성전자', 'LG전자', 'SK Hynix')
listInterest = list(interest)
print(listInterest, type(listInterest))

print("\n078")
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tupleInterest = tuple(interest)
print(tupleInterest, type(tupleInterest))

print("\n079")
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake

print("\n080")
even = tuple(range(2, 100, 2))
print(even)