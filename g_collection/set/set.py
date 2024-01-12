# set란 자료구조는? 중복이 없고, 순서가 없는 자료구조 입니다.
# - 순서가 없으면 자료를 가져올 수 없다. 값이 있는지 없는지 검사하기 위해 만들어짐

world_set = {'korea', 'america', 'japan', 'china'} # 특징 : 중괄호
print(type(world_set))
print(len(world_set))
# print(world_set[1]) # 오류 : 순서가 없어 가져올 수 없다. list로 형변환 할 경우 가능.
world_set.add('korea')
print(world_set) # 다른 자료구조를 통해 문자열로 보여주는 결과물이다. 순서가 다르게 보여질 수 있음.

# 중복을 제거할 때 효과적이다.
# set으로 형변환해서 다시 list로 가져오면 중복삭제할 수 있다. (코딩테스트에서 많이 나옴)
datas = [1, 3, 1, 2, 3, 3, 4]
print(list(set(datas)))
