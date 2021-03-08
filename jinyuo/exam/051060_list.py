# https://wikidocs.net/7023

print("051")
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

print("\n052")
movie_rank.append("배트맨")
print(movie_rank)

print("\n053")
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

print("\n054")
movie_rank.remove("럭키")
print(movie_rank)

print("\n055")
del movie_rank[2]
print(movie_rank)
del movie_rank[2]
print(movie_rank)

print("\n056")
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang1 += lang2
print(lang1)

print("\n057")
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"min : {min(nums)}")
print(f"max : {max(nums)}")
 
print("\n058")
nums = [1, 2, 3, 4, 5]
print(sum(nums))

print("\n059")
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

print("\n060")
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))
