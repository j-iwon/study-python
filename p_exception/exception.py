# try:
#     number = int(input('정수를 입력하세요.'))
#
# except ValueError as e: # ValueError(class)타입인지 확인 후 e에 담는다.
#     print('정수만 입력해주세요!')
#
# print('반드시 실행되어야 하는 문장')

# try:
#     print(10 / 0)

# except ZeroDivisionError as e: #ZeroDivisionError 에러코드를 e에 담음 에러메세지를 문자로 return
#     print(e)
#     print('0으로 나눌 수 없습니다.')

# except: #모든 에러코드를 받음 Exception 이 생략되어있음. Exception은 모든 에러코드의 부모
#     print('0으로 나눌 수 없습니다.')

# datas = [1, 2, 3]
# try:
#     print(datas[3])
#     #위의 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요!')
#
# except ValueError:
#     pass
#
# except IndexError:
#     print('인덱스를 확인해주세요!')
#
# else:
#     # try에 작성한 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요!')
#
# finally:
#     print('반드시 실행되어야 하는 문장')

class BadWordError(Exception):
    def __str__(self):
        return "비속어는 사용할 수 없습니다."


def check_bad_word(message):
    if '멍청이' in message:
        raise BadWordError


chat = input('채팅: ')
try:
    check_bad_word(chat)
    print(chat)
except BadWordError as e:
    print(e)
