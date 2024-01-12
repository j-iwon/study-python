# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시 1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시 1
# [1000, 2000]

# 입력 예시 2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시 2
# [700, 2800, 3500]

# 출력할 예시 금액을 리스트에 담는다

# 강사님 풀이

def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')


# #지원 풀이
# pay = [2000, 4000, 6000]
# #
# def order_info(*args, **kwargs):
#     pay_list = args
#     number = len(pay_list)
#     count = kwargs.get('count')
#     sale = int(kwargs.get('coupon')) /100
#
#     result = [int(pay_list[num] - (pay_list[num]* sale)) if num < count else pay_list[num] for num in range(number)]
#     print(result)
#
# order_info(*pay, coupon=50, count=0)
