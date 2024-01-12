student = {
        "name": "박지원",
        "email": "nnzu0521@gmail.com"
}

print(student['name'])
print(student.get('name')) #두가지 방식으로 출력 가능
# print(student.get['name']) # 오류

# get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
print(student.get('phone','01091292519'))
# default 값이 없을 때에는 None을 가져온다.
print(student.get('adress'))


# 'name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다.
student['name'] = '지원'
# 'phone' key값이 없기 때문에, 아래의 코드는 '추가'이다.
student['phone'] = '01091292519'
print(student)

if 'email' in student: #수정
        student['email'] = 'by13525@naver.com'
else: #추가
        student['email'] = 'giwon0531@gmail.com'
print(student)

my_dict = {
    1: "한동석",
    "two": "20살",
    False: [10, 20, 30],
    "row": [
        {"name": "ted", "age": 40},
        {"name": "jack", "age": 30},
        {"name": "john", "age": 20}
    ]
}

# row에 있는 회원 3명의 정보를 모두 출력
if 'row' in my_dict:
        # print(type(my_dict["row"])) #type을 먼저 확인
        for data in my_dict['row']:
                print(f"{data['name']}, {data['age']}")

# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면 홀수만 출력한다.
# dict를 사용한다.

# 방법 1
number_dict = {
        "짝수":[i * 2 for i in range(5)],
        "홀수":{(i + 1) * 2 for i in range(5)}
}
# 방법 2
number_dict = {
    True: [i * 2 + 1 for i in range(5)],
    False: [(i + 1) * 2 for i in range(5)]
}

# 방법 1
print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ')])))
# 방법 2
print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ') == '홀수'])))

student = {
        "name": "박지원",
        "email": "nnzu0521@gmail.com"
}

# key 분리
print(list(student.keys()))

# value 분리
print(list(student.values()))

# item 분리
print(list(student.items())) # list 안에 tuple

for key, value in student.items(): #반복문을 사용하여 가져오기
        print(key, value)
