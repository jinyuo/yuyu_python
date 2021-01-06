# https://wikidocs.net/7030

print("111")
string = input();
print(string * 2)

print("\n112")
num = input("숫자를 입력하세요 : ")
print(int(num) + 10)

print("\n113")
num = input("숫자를 입력하세요 : ")
if int(num) % 2 == 0:
    print("짝수")
else:
    print("홀수")

print("\n114")
num = input("입력값 : ")
temp = int(num) + 20
if temp <= 255:
    print(f"출력값 : {temp}")
else:
    print(255)

print("\n115")
num = input("입력값 : ")
temp = int(num) - 20
if temp < 0:
    print(0)
elif temp > 255:
    print(255)
else:
    print(f"출력값 : {temp}")

print("\n116")
curTime = input("현재 시간(hh:mm) : ")
if curTime.split(":")[1] == "00": # curTime[-2:]
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

print("\n117")
fruit = ["사과", "포도", "홍시"]
string = input("좋아하는 과일은? ")
if string in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

print("\n118")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
string = input("투자 종목 : ")
if string in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

print("\n119")
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
string = input("제가 좋아하는 계절은 : ")
if string in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다")

print("\n120")
string = input("좋아하는 과일은?")
if string in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")