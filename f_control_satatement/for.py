# for i in range(1,11,1): ## i는 index의 약자
#     print(f'{i + 1}. 박지원')
#
# for i in range(1,11):
#     print(f'{i}.지원')
#
# for i in range(10,0,-1):
#     print(f'{i}. 원')

# for i in range(10):
#     # pass            #비워놓으면 오류가 나기 때문에 당장 값을 입력하지 않을때 사용
#     print(f'{i+1}')

# for i in range(10):     #시작값은 0으로 잡는것이 좋다. 그럼 거꾸로 줄어들 때에는?
#     print(f'{10 - i}')

# 1~10까지 중 3까지만 출력

for i in range(10):
    print(i + 1)
    if i == 2:
        break

# 1~10까지 중 4를 제외하고 출력

for i in range(10):
    if i == 3:
        continue # 특정 조건에서 continu 밑을 출력하고싶지 않을 때
    print(i + 1)