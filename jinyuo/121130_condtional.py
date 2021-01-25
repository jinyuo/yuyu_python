# # https://wikidocs.net/7031

print("121")
char = input("알파벳 : ")
if char.islower():
    print(char.upper())
else:
    print(char.lower())

print("\n122")
score = int(input("score : "))
if score <= 20 and score >= 0:
    grade = "E"
elif score <= 40:
    grade = "D"
elif score <= 60:
    grade = "C"
elif score <= 80:
    grade = "D"
else:
    grade = "A"
print(f"grade is {grade}")

print("\n123")
money = input("입력 : ")
money = money.split(" ")
if money[1] == "달러":
    money[0] = 1167*float(money[0])
elif money[1] == "엔":
    money[0] = 1.096*float(money[0])
elif money[1] == "유로":
    money[0] = 1268*float(money[0])
elif money[1] == "위안":
    money[0] = 171*float(money[0])
print(f"{money[0]} 원")

print("\n124")
number = []
for i in range(0, 3):
    number.append(input(f"input number{i} : "))
print(max(number))

print("\n125")
carrier = {"011" : "SKT", "016" : "KT", "049" : "LGU", "010" : "unknown"}
phone = input("휴대전화 번호 입력 : ").split("-")
print(f"당신은 {carrier[phone[0]]} 사용자입니다.")

print("\n126")
zipcode = input("우편번호")
if zipcode[2] in ["0", "1", "2"]:
    print("강북구")
elif zipcode[2] in ["3", "4", "5"]:
    print("도봉구")
elif zipcode[2] in ["6", "7", "8", "9"]:
    print("노원구")

print("\n127")
idnumber = input("주민등록번호 : ")
if idnumber[7] in ["1", "3"]:
    print("남자")
elif idnumber[7] in ["2", "4"]:
    print("여자")

print("\n128")
idnumber = input("주민등록번호 : ")
print(int(idnumber[8:11]))
if 0 <= int(idnumber[8:11]) < 9:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

print("\n129")
checksum = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
idnumber = input("주민등록번호 : ").replace("-", "")
for i in range(0, 12):
    checksum[i] = int(idnumber[i]) * checksum[i]

if 11 - sum(checksum) % 11 == int(idnumber[12]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

print("\n130")
import pip._vendor.requests
btc = pip._vendor.requests.get("https://api.bithumb.com/public/ticker/").json()['data']
fluctuation = int(btc["max_price"]) - int(btc["min_price"])
if int(btc["opening_price"]) + fluctuation > int(btc["max_price"]):
    print("상승장")
else:
    print("하락장")