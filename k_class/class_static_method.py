class Student:
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    @staticmethod
    def print_start_time_of_study(): #객체(self)로 접근하는 메소드가 아니라면 staticmethod로 데코레이터 선언하여 사용
        print("9시 땡")               # self를 지우고 @staticmethod : 객체가 아니라 class로 직접 접근하여 컴파일됨
        Student.status = '공부 중'

print(Student.status)

Student.print_start_time_of_study()

print(Student.status)