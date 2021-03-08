# https://wikidocs.net/7028

print("101")
print("bool")

print("\n102")
print(3 == 5)
print("false")

print("\n103")
print(3 < 5)
print("true")

print("\n104")
x = 4
print(1 < x < 5)
print("True")

print("\n105")
print ((3 == 3) and (4 != 3))
print("True")

print("\n106")
# print(3 => 4)
print(3 >= 4, "비교문의 => 를 >=로 수정")

print("\n107")
if 4 < 3:
    print("Hello World")
print("출력 없음")

print("\n108")
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
print("Hi, there.")

print("\n109")
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
print("1\n2\n4")

print("\n110")
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
print("3\n5")