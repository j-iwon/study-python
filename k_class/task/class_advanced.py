# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
class User:
    # # private: 자신의 클래스에서만 접근 가능
    # # 1. 외부에서 접근하지 말자!
    # # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    # __user_number = 0
    number1 = 0

    def __init__(self, user_id, user_password, user_name):
        User.number1 += 1
        self.user_number1 = User.number1
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name

    @staticmethod
    def get_number():
        return User.number

    @classmethod
    def set_admin(cls, **kwargs):
        kwargs['user_id'] = 'admin_' + kwargs['user_id']
        return cls(**kwargs)


user = User('nunu','1234','박지원')
user2 = User('tutu','1234','박지원')

print(user.user_id, user2.user_id)

admin = User.set_admin(user_id='mumu', user_password='1234', user_name='지원')
admin2 = User.set_admin(user_id='mumu', user_password='1234', user_name='지원')
admin3 = User.set_admin(user_id='mumu', user_password='1234', user_name='지원')
admin4 = User.set_admin(user_id='mumu', user_password='1234', user_name='지원')
print(admin.user_id)

print(User.number1)











