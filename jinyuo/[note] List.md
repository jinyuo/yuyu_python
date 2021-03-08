# 리스트

생성일: 2021년 1월 24일 오전 12:37

## 선언

빈 리스트 선언 가능

```python
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
```

리스트 내 요소가 될 수 있는 자료형에는 제한이 없다.

초기화와 동시에 선언 시, 각 요소의 데이터형이 달라도 선언 가능
리스트 또한 리스트의 요소일 수 있음

## 추가

### append()

리스트의 마지막에 요소 추가

```python
movie_rank.append("배트맨")
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
```

### insert(n, value)

리스트의 n 번째 위치에 value 삽입

```python
movie_rank.insert(1, "슈퍼맨")
# movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
```

## 삭제

### remove(value)

리스트 내 존재하는 value 중 첫 번째 value를 제거

```python
movie_rank.remove("럭키")
# movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "배트맨"]
```

### del list[n]

리스트 내 n 번째 요소 제거

```python
del movie_rank[2]
# movie_rank = ["닥터 스트레인지", "슈퍼맨", "배트맨"]
```

## 연산

### +

2개의 리스트를 합친다.

```python
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang1 += lang2
# lang1 = ["C", "C++", "JAVA", "Python", "Go", "C#"]
```

## 함수

### min()

리스트의 최소값 반환

```python
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"min : {min(nums)}")
# 1
```

### max()

리스트의 최대값 반환

```python
print(f"max : {max(nums)}")
# 7
```

### sum()

리스트 내 모든 요소의 합계 반환

```python
nums = [1, 2, 3, 4, 5]
print(sum(nums))
# 15
```

### len()

리스트의 길이 반환

```python
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
# 12
```

### "string".join(list)

리스트의 각 요소 사이에 지정한 문자열을 붙여 하나의 문자열을 반환

```python
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
```

### sort()

리스트의 요소를 순서대로 정렬

```python
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
# [1, 2, 3, 4, 5, 9, 10]
```

## 슬라이싱

[시작 인덱스, 마지막 인덱스, 오프셋]

문자열 슬라이싱과 유사하다.

```python
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
# [100, 130, 140, 150, 160, 170]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
# [1, 3, 5, 7, 9]

# 역순
print(nums[::-1])
```

## 인덱싱

```python
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])
```