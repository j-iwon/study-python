# # print(list("ABC"))
#
# # for i in "ABC":
# #     print(i)
#
# # upper(), lower()
print("Apple123".upper())
print("Apple123".lower())
#
# # split()
# data = "사과, 바나나, 파인애플, 포도, 복숭아"
# data.split(",", maxsplit=2)
# print(("A B C D E F").split())
# print("A       B".split(" "))
#
# # join() # 안에 있는 요소들을 동일한 구분점으로 연결할 때 사용
# print(":".join(['a','b','c'])) # 문자열 값으로 연결되어 나온다
# print("".join(['a', 'b', 'c']))
#
# # replace('기존 값', '새로운 값') #기존 값을 새로운 값으로 연결할 때 사용
# print("A b C d".replace(" ",""))
#
# # strip(), lstrip(), rstrip() #l은 왼쪽 r은 오른쪽끝 : 앞뒤 공백을 제거할 때 보통 사용한다.
# print("a   b c        ".strip())
# print("a   b c        ".strip(" ")) #사이 사이는 삭제하지 않음
# print("apple".strip("a"))
#
# # index : 찾고자 하는 값이 없으면 오류가 발생한다.
# print("ABC".index("A"))
# ## print("ABC".index("Z")) # 오류 ValueError: substring not found
#
# # find() : 찾고자 하는 값이 없으면 -1을 가져온다.
# print("ABC".find("A"))
# print("ABC".find("Z")) # 없다는 것도 표현해줌
#
# # in : 값의 유무 검사
# print("A" in "ABC")
# print("Z" in "ABC")
#
# # count() : 전달한 값이 몇 개 있는지 검사
# print("fmdsklfmldksmfoiejwonfodsnjkfnoieqnofnip".count("o"))

#
s = "189,000원"
#정수만 나오게
# for i in s:
#     if '0' <= i <= '9': #조건식에서는 문자열이 자동으로 정수로 인식되어 연산이 된다, 단 '0'와 같이 조건 맞춰주기 0 < i < 9 는 오류
#         print(i, end='')

# print("".join([i for i in s if '0' <= i <= '9']))

