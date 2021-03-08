# https://wikidocs.net/7022 풀이

print("021")
letters = 'python'
print(letters[0], letters[2])

print("\n022")
license_plate = "24가 2210"
string_length = len(license_plate)
print(license_plate[string_length-4:string_length])
# print(license_plate[-4:])

print("\n023")
string = "홀짝홀짝홀짝"
for x in range(0, len(string)):
    if x % 2 == 0:
        print(string[x])
# print(string[::2])

print("\n024")
string = "PYTHON"
print(string[::-1])

print("\n025")
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

print("\n026")
phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))

print("\n027")
url = "http://sharebook.kr"
print(url.split(".")[-1])

print("\n028")
lang = 'python'
try:
    lang[0] = 'P'
except:
    print("Error")

print(lang)
# Error

print("\n029")
string = 'abcdfe2a354a32a'
print(string.replace('a', "A"))

print("\n030")
string = 'abcd'
string.replace('b', 'B')
print(string)
# abcd
