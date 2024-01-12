# 1. 성적 산출 프로그램을 만드시오.
# 90 ~ 100점 : A
# 80 ~ 89점 : B
# 70 ~ 79점 : C
# 그 외 : F

score = int(input('성적을 입력하세요: '))

if score>= 90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
else:
    print('F')

# 2. for문을 사용하여 다음과 같은 모양을 출력하시오
# *
# **
# ***
# **
# *

for i in range(1,4):
    print('*'* i)
for i in range(3,0,-1):
    print('*'* i)

# 3. 1000보다 큰 정수에서 가장 작은 37의 배수는 무엇인가요?

num = 1000
while (num % 37 !=0 ) & ( num >= 1000):
    num += 1

print(num)