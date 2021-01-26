# 문자열

생성일: 2021년 1월 24일 오전 12:37

### 특수 문자 무시

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

### 이스케이프 문자

- \n : 줄바꿈
- \t : 들여쓰기

# print 함수

## 전달하는 매개변수가 여러 개인 경우

공백 없이 출력

```python
# 오늘은일요일
print ("오늘은", "일요일")
```

## 옵션

### sep; 구분자

매개변수를 구분하는 문자열 지정 ⇒ 매개변수 사이에 지정한 문자열 포함

sep 옵션 생략 시, sep=""와 같다.

```python
# naver;kakao;sk;samsung
print("naver", "kakao", "sk", "samsung", sep=";")
```

### end;

출력문 끝의 문자열 지정

생략 시 end="\n"와 같다.

```python
# firstsecond
print("first", end="");print("second")
```

; : 한 줄에 여러 개의 명령을 작성하기 위함