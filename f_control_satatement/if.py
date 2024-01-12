# number = 15
#
# if number % 3 == 0:
#     print(f'{number}는 3의 배수입니다.')
# if number % 5 == 0:
#     print(f'{number}는 5의 배수입니다.')


## number가 양수인지, 음수인지, 0인지 검사

# number = int(input('숫자를 입력하세요: '))
#
# if number > 0:
#     print(f'\n입력하신 {number}는 양수입니다.')
# if number == 0:
#     print(f'\n입력하신 {number}는 0입니다.')
# if number < 0:
#     print(f'\n입력하신 {number}는 음수입니다.')

# number = 0
#
# positive_condition = number > 0
# negative_condition = number < 0
#
# if positive_condition:
#     print(f'{number}는 양수입니다.')
# elif negative_condition:
#     print(f'{number}는 음수입니다.')
# else:
#     print(f'{number}')

##나이를 입력받은 후 미성년자인지 검사해라.

# message = '나이를 입력하세요: '
# age = int(input(message))
#
# child = 0 < age < 20
# error_child = age <= 0
#
# if child:
#     print('미성년자입니다.')
# elif error_child:
#     print('잘못 입력하셨습니다.')
# else:
#     print('성인입니다.')

##두 정수를 입력받은 후 대소비교 진행

message = "두 정수를 입력하세요: "
number, number2 = map(int,input(message).split())
#선언할 때 넣을 값을 모를 경우 초기값을 넣어준다.
# 정수: 0
# 실수: 0.0
# 문자열: '' 또는 ""
# 불린: False
result_message = ''

#일괄처리란,
#각 분기별로 결과를 처리하지 않고
#모든 분기 종료 후 한번에 처리하는 것을의미한다.

if number < number2:
    result_message = f'{number}가(이) {number2}보다 작습니다.'
elif number != number2: # number > number2
    result_message = f'{number}가(이) {number2}보다 큽니다.'
else:
    result_message = f'{number}와 {number2}는 같습니다.'
print(result_message) #print 일괄처리