# 변수

생성일: 2021년 1월 24일 오전 12:37

객체(자료형)를 가리키는 것

### 선언

변수명으로 한글 사용 가능

튜플 또는 리스트로 변수에 값 할당 가능

```python
삼성전자 = 50000

# 네 가지 경우 모두 a = 'python' , b = 'life'
a, b = 'python', 'life'
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
```

### 자료형

```python
# <class 'int'>
PER = 15.79

# <class 'str'>
a = "132"

# 자료형 출력
print(type(a))

# <class 'float'>
float_num = 15.79
```

### 메모리 주소 확인

```python
id(a)
# 변수가 가리키는 객체의 주소 값을 반환
```

## 리스트 복사

### 1. 단순 할당

```python
a = [1,2,3]
b = a
```

위 코드에서 a와 b는 같은 객체를 가리킴 → a와 b는 동일함

```python
# 동일한 객체를 가리키는지를 bool으로 반환
# True
a is b 
```

### 2. [:] 이용

[:] : 리스트 전체 가리킴

```python
a = [1,2,3]
b = a[:]
```

a와 b 서로 영향 없음

### 3. copy 모듈 이용

```python
# copy 모듈 사용
from copy import copy

# b = a[:]와 동일
b = copy(a)
```