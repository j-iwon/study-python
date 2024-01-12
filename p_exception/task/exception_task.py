# 캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여, 발생시 안내 메세지까지 출력하기

class NicknameError(Exception):
    def __str__(self):
        return '올바르지 못한 단어를 사용하였습니다.'

def check_nickname(nickname):
    not_allowed_names = ['바보', '멍게', '해삼', '운영자']
    for name in not_allowed_names:
        if name in nickname:
            raise NickNameError


nickname = input('닉네임: ')
try:
    check_nickname(nickname)
    print(f'어서오세요 {nickname}님')

except NickNameError as e:
    print(e)