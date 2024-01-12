# f(x) = 2x+1

# def f(x): # 함수명은 동사로
#     return 2 * x + 1  # return은 무조건 값이 1개
#
# result = f(2)
# print(result)

# 두 정수의 곱셈
# def multiple(num1, num2):
#     result = num1 * num2
#     return result

# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def divide(num1, num2):
#     if num2 != 0:
#         return num1 // num2, num1 % num2
#     return None

# result = divide(10, 3)
# if result:
#     value, rest = result
#     print(f'몫: {value}, 나머지: {rest}')
# else:
#     print('0으로 나눌 수 없습니다.')

# 1~10까지 print()로 출력하는 함수
# def print_from1_to10():
#     for i in range(10):
#         print(i + 1, end=' ')
# print_from1_to10()

# 이름을 n번 print()로 출력하는 함수
# def print_name_n(name,count):
#     for i in range(count):
#         print(name)

# 1~n까지 합을 구해주는 함수
# def get_total_from1(end):
#     total = 0
#     for i in range(end):
#         total += i + 1
#     return total


# 1~100까지 중 n의 배수를 print()로 출력하는 함수
# def print_time_from_1_to100(number):
#     for i in range(100):
#         if (i + 1) % number == 0:
#         print(i + 1)

# 세 정수의 뺄셈 함수
# def sub(number1, number2, number3):
#     return number1 - number2 - number3


# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수

# def get_count_of_result(target, keyword):
#     # return len([i for i in target if i == keyword])
#     for i in target:
#         count = 0
#         if i == keyword:
#             count += 1
#     return count

'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수
'''

# def find(target, keyword):
#     for i in range(len(target)):
#         if target[i] == keyword:
#             return i
#
#     return -1


