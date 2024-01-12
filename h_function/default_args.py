# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정할 수 있고, arg=value로 작성한다.
def sub(numver1, number2, number3, number4=0): # 들어올지 안 들어올지 모르는 부분에 초기값을 설정해주면 된다.
    return numver1 - number2 - number3 - number4

result = sub(1,2,3)
print(result)

# 실습
# 이름을 전달받지 못하면 '익명'으로 대체하고,
# 나이를 전달받지 못하면 '0'으로 대체한다.
