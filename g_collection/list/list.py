animals = ["dog", "cat", "bird", "fish"]
print(animals)
print(type(animals))

# 인덱스로 접근    ## 왜 인덱스는 0부터 시작할까? 시작 주소를 잡고있기 때문에 0부터 시작한다
print(animals[1])
print(animals[2])

# 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
print(animals[-1])
print(animals[-2]) ## 언제 사용하는지? 많은 값 중에 제일 최신된 값을 가져오고 싶을 때 굳이 인덱스 값을 계산하지 않아도 음수 첫번째로 뽑으면 된다.

# len()
print(len(animals))

# append()
animals.append("hamster")
print(len(animals))
print(animals)

animals.append("cat")
print(animals)    ## list는 중복을 신경쓰지 않는다.

# insert()
animals.insert(1, "dog")
print(animals)

# remove()
animals.remove("fish")
print(animals)

# del()
del(animals[1]) #방법1

del animals[1] #방법2
print(animals)

# clear()
animals.clear()
print(animals)

# #index()
print(animals.index('bird'))
print(animals.index('tiger')) #없는걸 검색하면 오류

# 수정
animals[animals.index('bird')] = 'lion' # 대괄호 안에는 인덱스 번호만 들어갈 수 있다.

index = animals.index('bird') # 먼저 검색하고 지정한 후 수정하면 더 보기 편하다
animals[index] = 'lion'
print(animals)

# 그 외
animals = ["dog", "cat", "bird", "fish"]
print(animals * 2)

print('dog' in animals)
print('tiger' in animals)   # 인덱스를 검색할 때 훨씬 간편하게 보는 법

for animal in animals: # animals = ["dog", "cat", "bird", "fish"] 리스트를 편하게 볼 수 있음
    print(animal)






# 실습
# 1~98까지 list에 담고 출력

number_list = [0] * 90

for i in range(len(number_list)):           #풀이 1
    number_list[i] = i + 1y_

number_list = []                           #풀이 2
for i in range(90):
    number_list.append(i + 1)
print(number_list)

# 1~100까지 중 짝수만 list에 담고 출력

number_list = [0] * 50                    #풀이
for i in range(len(number_list)):
    number_list[i] = (i + 1) * 2
print(number_list)

# 1~10까지 list에 담은 후 짝수만 출력

# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제

list = ['지원','규일','우람','시현']
list[1] = '유진'
del list[3] #풀이 2 : del list[-1]
print(list)

# list 안에 list
number_list = [[1,3,5],[2,4,6]]
# print(number_list[0][0])

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])