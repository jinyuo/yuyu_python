# https://wikidocs.net/7025

print("061")
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

print("\n062")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

print("\n063")
print(nums[1::2])

print("\n064")
print(nums[::-1])

print("\n065")
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

print("\n066")
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

print("\n067"),
print("/".join(interest))

print("\n068")
print("\n".join(interest))

print("\n069"),
string = "삼성전자/LG전자/Naver"
string_list = string.split("/")
print(string_list)

print("\n070")
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
