# 인덱스 슬라이싱 : 반복문을 쓰지 않아도 원하는 부분을 추출할 수 있다.
animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start=0 : exclusice_end=len(list)] -> list
print(animals[0])
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])

# list[inclusive_start=0 : exclusice_end=len(list) : step=1] * step은 메모리를 많이 소모하여 잘 쓰지 않음
food = ['noodle', 'meat', 'bread', 'chicken']
print(food[:3:2])
print(food[2::2])

# 역순 출력
print(food[::-1])

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list = list(range(1,11))
print(number_list)

# [1, 3, 5, 7, 9]
num_list = list(range(1,10))
print(num_list[::2])

# [6, 5, 4, 3, 2]
print(num_list[5:0:-1])

# [2, 4, 6]
print(num_list[1:6:2])

# [2, 3, 4, 5, 6, 7]
print(num_list[1:7])

animals = ['dog', 'dog', 'cat', 'bird'] # 슬라이스를 저장공간으로 써보자

# 기존 값은 사라지고 zoo list 안에 있는 요소가 각각 들어간다. # 교체
animals[1:2] = zoo
print(animals)

# 기존 값은 뒤로 밀리고 해당 자리에 값이 들어간다. # 삽입
animals.insert(animals.index('dog') + 1, 'giraffe')
print(animals)

# 기존 값은 뒤로 밀리고 zoo list 통채로 들어간다.
animals.insert(animals.index('dog') + 1, zoo)
print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']

del animals[animals.index('cat')]
# animals.remove('cat')
print(animals)

animals[-2: -3: -1] = ['whale']
print(animals)

animals.insert(animals.index('dog') + 1, 'fish')
print(animals)

animals.insert(animals.index('dog') + 1, 'hamster')
print(animals)

animals[1:3] = ['hamster', 'fish', 'dog']
print(animals)
