# 문자열

생성일: 2021년 1월 24일 오전 12:37

immutable 함 → 수정 불가

## 특수 문자 무시

- \ 사용

    ex) \' → '

- " 또는 ' 인 경우에는 구분하여 사용

```python
# Mary's cosmetics
print("Mary\'s cosmetics")
print("Mary's cosmetics")

# 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')
```

## 이스케이프 문자

- \n : 줄바꿈
- \t : 들여쓰기

## print 함수

### 전달하는 매개변수가 여러 개인 경우

공백 없이 출력

```python
# 오늘은일요일
print ("오늘은", "일요일")
```

### 옵션

**sep; 구분자**

매개변수를 구분하는 문자열 지정 ⇒ 매개변수 사이에 지정한 문자열 포함

sep 옵션 생략 시, sep=""와 같다.

```python
# naver;kakao;sk;samsung
print("naver", "kakao", "sk", "samsung", sep=";")
```

**end;** 

출력문 끝의 문자열 지정

생략 시 end="\n"와 같다.

```python
# firstsecond
print("first", end="");print("second")

# ; : 한 줄에 여러 개의 명령을 작성하기 위함
```

## 인덱싱

문자열 내 특정한 값을 뽑아냄

시작값은 0

### n번째 값

```python
letters = 'python'
print(letters[0], letters[2])
# pt
```

## 슬라이싱

문자열 내 지정하는 부분을 잘라냄

문법 : [시작 인덱스:끝 인덱스:오프셋] 

음수 값인 경우에는 문자열의 맨 뒤부터 역순으로 셈

```python
# 끝에서 4번째부터 끝까지
license_plate = "24가 2210"
print(license_plate[-4:])
# 2210

# 오프셋 활용
string = "홀짝홀짝홀짝"
print(string[::2])
# 홀홀홀

# 역순
print(string[::-1])
```

## replace 함수

replace("old", "new") : old 문자열을 new 문자열로 변환

```python
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
# 010 1111 2222
```

## split 함수

split("문자열") : 문자열을 매개변수값을 기준으로 구분한 배열로 반환

```python
url = "http://sharebook.kr"
print(url.split(".")[-1])
# kr
```