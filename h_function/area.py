# 전역 변수(global variable)
#    : 지역 밖에 선언된 변수
#    : 여러 함수에서 공유해야하는 값이 있을 경우 사용
# 지역 변수(local variable)
#    : 어떤 지역 안에 선언된 변수

# 구분하는 방법 : 어디에서 선언 되었는가?

count = 0 #전역 변수
def increase():
    # print(count)
    # 지역 변수
    # count = 0
    global count # 전역 변수를 수정하려면 global 키워드를 사용한다.
    count += 1 # 전역 변수가 수정된다.

increase()
print(count)