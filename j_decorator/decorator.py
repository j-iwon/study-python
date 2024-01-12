# import datetime
#
# def log_time(original_function): #1. 주변로직 함수 먼저 만들기
#     print('log_time 들어옴')
#
#     def logging(*args):
#         print('logging 들어옴')
#         print(args)
#         print(datetime.datetime.now())
#         print('logging 함수 종료')
#         return original_function(*args)
#
#     print('log_time 함수 종료')
#     return logging
#
#
# @log_time
# def add(*args):
#                     # 원래 이 자리에 들어가야할 함수들을
#                     # 데코레이터를 통해 @log_time 으로 만듦
#     total = 0
#     for i in args:
#         total += i
#
#     return total
#
# result = add(1, 2, 3)
# print(result)


# ((결과))
# 에드 함수를 실행한 순간
# log_time 들어옴              # 데코레이터 자동 실행
# log_time 함수 종료           # 로깅을 사용하기 위해 로그타임이 한 번 실행됨
# logging 들어옴              # 로깅 실행
# (1, 2, 3)
# 2024-01-05 14:25:40.407761
# logging 함수 종료            # 로깅 실행 완료
# 6                          # 에드 함수 결과값 출력

# # -------------------------------------------------------------------
# 평균(주변로직)을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다. 데코레이터에서 검사하는 함수 1 *args (여러개의 정수)
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다. 데코레이터에서 검사하는 함수 2 **kwargs (합과 개수)
# 총 합을 구하는 함수를 (메인로직) 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.

def average(original_function):
    def operate(*args, **kwargs):
        count = len(args)
        if count != 0:
            total = 0
            for i in args:
                total += i

        else:
            total = kwargs.get('total')
            count = kwargs.get('count')

        print(f"평균: {total/count}")
        return original_function(*args, **kwargs)
    return operate

@average
def set_datas(*args, **kwargs):
    total = 0
    for i in args:
        total += i
        print(f"총 합: {total if total != 0 else kwargs.get('total')}")

    set_datas(1, 2, 3, 4, 5)
    set_datas(total=100, count=5)



