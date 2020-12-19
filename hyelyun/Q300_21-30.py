# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:57:55 2020

@author: you
"""

# 021 문자열
letters = 'python'
print(letters[0], letters[2])

# 022 문자열
license_plate = "24가 2210"
print(license_plate[-4:])

# 023 문자열
string = "홀짝홀짝홀짝"
print(string[::2])

# 024 문자열
string = "python"
print(string[::-1])

# 025 문자열
phone_number = "010-1111-2222"
phone_number2 = phone_number.replace("-", " ")
print(phone_number2)

# 026 문자열
phone_number3 = phone_number.replace("-", "")
print(phone_number3)

# 027 문자열
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split)
print(url_split[1])
print(url_split[-1])

# 028 문자열
lang = 'python'
'''
오류
lang[0] = 'P'
'''
print(lang)


# 029 문자열
string = 'abcdef2a354a32a'
string2 = string.replace("a", "A")
print(string2)

# 030 문자열
string = "abcd"
string.replace("b","B")
print(string)
'''
출력 결과 : abcd
문자열은 변경할 수 없는 자료형
replace 메서드를 사용하면 원본은 그대로 둔채 변경된 새로운 문자열 객체를 리턴함
'''