# 1~15까지 출력
# for i in range(15):
#     print(f'{i + 1}')

# 30~1까지 출력
# for i in range(30):
#     print(f'{30 - i}')

# 1~100까지 중 홀수만 출력
# for i in range(0,100,2): # 내가 한거
#     print(f'{i + 1}')

# for i in range(50):   # 강사님이 한거
#     print(i * 2 + 1, end=' ')

# 1~10까지 합 출력
# sum=0
# for i in range(11) :
#     sum += i
# print(sum)

# 1~n까지 합 출력
# sum=0
# n = int(input('n을 입력하세요:'))
# for i in range(1,n+1):
#     sum += i
# print(sum)

# message1 = '1부터 n까지의 합'
# message2 = 'n: '


# 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(3):
#     for x in range(3,7):
#         print(x, end=' ')

# for i in range(12):
#         print(i % 4 + 3, end=' ')

# '1,235,500'를 1235500으로 출력
# data = '1,235,500'
# result = ''
# for i in data:
#     if i != ',':
#         result += i
#
# result = int(result)
# print(result + 5)

# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다.
title = "색상은 골라주세요!\n"
menu = "1. 빨간색\n" \
       "2. 검은색\n" \
       "3. 노란색\n" \
       "4. 흰색\n"

choice = int(input(title + menu))
choice1, choice2, choice3, choice4 = choice == 1, choice == 2, choice == 3, choice == 4
color1, color2, color3, color4 = "red", "black", "yellow", "white"
result = None

if choice1:
    result = color1
elif choice2:
    result = color2
elif choice3:
    result = color3
elif choice4:
    result = color4

print(result)


