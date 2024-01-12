
## 연산과 연결 구분하기

# print('안'+'녕') ##문자열 끼리만 (+) 는 연결, (*) 는 반복
# print('바이'*2)
#
# data = 2
# print('바' + str(data))

# name = input("이름:  ")
#
# formatting = f'{name}님 환영합니다 !'
# print(formatting)

##실습
## 제 이름은 ???, 키는 ???cm 입니다.

# name = input("이름: ")
# height = input("키: ")
#
# formatting = f'제 이름은 {name}, 키는 {height}cm 입니다.'
# print(formatting)

##두 정수를 입력받은 후 곱셈 결과 출력

# print("곱하기 시작~ !")
# num = int(input("숫자1 :"))
# num2 = int(input("숫자2 :"))
# total = num * num2
# formatting = f'{num} x {num2} = {total}'
# print(formatting)

## 'A,B,C'.split(',') -> 결과 [ 'A', 'B', 'C' ] ##split = 잘게 쪼개다 = 형태를 list 로 봐야한다.
## map(각각 어떻게 바꿀 것인가, []) > 여러개를 한 번에 바꿔주는 함수

# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
#
# print(formatting)


# 현재 시간을 입력하고 시와 분으로 분리하여 출력
print('='*20)
message = '현재 시간을 입력하세요.'
ex_message = '예) 11:30'
num1, num2 = map(int, input(message + '\n' + ex_message + '\n').split(':'))
formatting = f'{num1}시 {num2}분'
print(formatting)
print('='*20)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력'
print('='*20)
message = '핸드폰 번호를 입력하세요.'
ex_message = '예)010-9129-2519'
num1, num2, num3 = input(message + '\n' + ex_message + '\n').split('-')
formatting = f'처음: {num1}\n중간: {num2}\n끝: {num3}'
print(formatting)
print('='*20)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
print('='*20)
message = '이름과 나이를 입력하세요.'
ex_message = '예)박지원 20'
name, age = input(message + '\n' + ex_message + '\n').split()
formatting = f'{name}님의 나이는 {age}살'
print(formatting)
print('='*20)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
print('='*20)
message = '더하기 시작 ! 세 정수를 입력하세요.'
ex_message = '예)2/2/2'
num1, num2, num3 = map(int, input(message + '\n' + ex_message + '\n').split('/')) #Class.split()
result = num1 + num2 + num3
formatting = f'결과 : {num1} + {num2} + {num3} = {result}'
print(formatting)
print('='*20)

# 공부하는 법 코딩을 직접 해석하고 설명해보기