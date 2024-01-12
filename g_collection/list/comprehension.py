# Comprehension (컴프리헨션 : (어떤 뜻을) 내포[포함])
# 반복하거나 특정 조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension
# [표현식 for 항목 in interator (if 조건)]
number_list = [1, 2, 3, 4]
result_list = [num * 3 for num in number_list]
print(result_list)

# number_list = [1, 2, 3, 4]
# # [6, 12]
# # result_list = [number * 6 for number in number_list if number <=2] # 6의 배수
# result_list = [number * 3 for number in number_list if number % 2 == 0] # 짝수에 3을 곱한다
# print(result_list)

# [표현식 if 조건 else 표현식 for 항목 in interator] # if 조건이 참이면 앞의 표현식이 값, else 조건이 참이면 뒤의 표현식이 값

# [1, 6, 3, 12]
# number_list = [1, 2, 3, 4]
# result_list = [number * 3 if number % 2 == 0 else number for number in number_list] # for 앞 부분과 뒷 부분을 구분해서 볼 줄 알아야 한다.
#                                                                                     # if 조건에 해당하면 if 앞의 표현식을, 아니면 else의 표현식을
# print(result_list)

# 아래의 list에서 '양수'만 추출한 뒤 새로운 list에 담기
# number_list = [10, 20, 30, -20, -3, 50, -70]
#
# number = [num for num in number_list if num > 0]
# print(number)

# n개의 0으로만 채워진 list

message = '생성할 list의 칸 수: '
result = int(input(message))
# result = int(input('생성할 list의 칸 수: '))
result_list = [0 for i in range(result)]
# result_list = [0] * result
print(result_list)

# 제곱의 결과가 10보다 큰 결과만 담은 list
# number_list = [1, -2, 3, -4, 5]
#
# number_list = [1, -2, 3, -4, 5]
# result_list = [number for number in number_list if number ** 2 > 10]
# print(result_list)


# 0~9까지 중 3의 배수만 담은 list
#
# list = [number for number in range(10) if  number %3==0 and number > 0]
# print(list)