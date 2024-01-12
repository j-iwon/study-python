# mutable : 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1) # 실제로는 사용하지 않도록 하기 !

# immutable : 변할 수 없는
data_tuple1 = (1, 2, 3, 4) # 소괄호 안에 데이터를 여러개 담는 것
data_tuple2 = data_tuple1

# data_tuple2[0] = 10
# print(data_tuple2) # 오류 발생 : tuple은 한 번 값을 넣으면 수정할 수 없다.
# 목적에 맞게 쓰기 : list는 제한을 둘 수 없다. ex) 엘리베이터는 5인승이라 5칸만 필요한데 list는 무한 생성가능. list와 tuple을 목적에 맞게 사용하기

test = list(data_tuple2)
test[0] = 10
print(test) # list로 변경하면 변경할 수 있다

data_tuple2 = data_tuple1 + (5, 6) # tuple을 연결은 가능, 기존의 tuple이 변경되는건 아니고 연결된 새로운 tuple 생성되는것
print(data_tuple2)
print(data_tuple1)

datas = 1, 2
print(type(datas))
print(datas[0])

# tuple 은 실제로 사용하는 일이 많지 않지만, 다른 개발자가 만들어놓은 코드를 이해하기 위해 알아야한다
# tuple도 순서가 있다.

ERROR_CODE = 1,
print(type(ERROR_CODE[0])) # ,(콤마)를 사용하면 값이 1개여도 tuple. 괄호는 생략 가능
# 대문자로 되어있는 것은 상수를 의심할 수 있어야한다. Python은 상수가 없기 때문에 임의로 지정해서 사용
