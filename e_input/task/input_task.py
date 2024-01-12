#email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# print('--'*20)
#
# message = '이메일을 입력하시오. \n:'
# id, domain = input(message).split('@')
# formatting = f'\n아이디: {id}\n도메인: {domain}'
# print(formatting)
#
#
# print('--'*20)

# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.

'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''

yard_message = 'yard 입력: '
inch_message = 'inch 입력: '

yard = float(input(yard_message))
inch = float(input(inch_message))

# yard, inch = map(int, input(yard_message + '\n' + inch_message).split('\n'))
yard_cm = round(yard*91.44, 2)
inch_cm = round(inch*2.54, 2)

# formatting = f'\n{yard}는 {yard_cm}cm \n{inch}는 {inch_cm}cm'
# print(formatting)

yard_formatting = f'{yard} yard는 {yard_to_cm}cm'
inch_formatting = f'{inch} yard는 {inch_to_cm}cm'

print(yard_formatting, inch_formatting, sep='\n')

