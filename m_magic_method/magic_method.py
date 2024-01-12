class Magic_method:
    def __str__(self):
        return f'{self.__repr__()}, __repr__() 사용됨'

# 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
# print(Magic().__repr__())
# 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다.
# print(Magic().__str__())
# 따라서, 생략해서 작성하면 __str__()이 붙게된다.

print(Magic_method()) # __repr__() (레퍼런스)가 생략되어있다. 그래서 주소값만이 아닌 문자열로 정리되어 출력됨
# ---------------------------------------------------------------------------------------------------------------------
class Magic:
    def __init__(self, name):
        self.name = name

    # 초기화된 필드를 확인하고자 할 때 사용된다.
    def __str__(self):
        return f'name: {self.name}'

# def __str__(self):
#     return f'{self.__repr__()}, __repr__() 사용됨.'

# 개발자는 값이 제대로 할당되었는지 확인하는게 중요. __str__ 로 재정의 해놓으면 번거로움이 사라짐. 객체만 프린트해도 바로 확인할 수 있음.
# 재정의하는 목적 : 초기화된 필드를 확인하고자 할 때 사용된다.
# ---------------------------------------------------------------------------------------------------------------------
class Student:
    def __init__(self,number,score):
        self.number = number
        self.score = score

    def __add__(self, other): # std1.score + std2.score 을 표현
        return self.score + other.score # other라는 객체를 받아 사용

    def __eq__(self, other): # self는 나, other은 비교할 대상
        # 주소를 먼저 비교
        if self.__repr__() == other.__repr__():
            return True
        # 주소가 달랐을 때 타입이 같은지 비교
        # isinstance(객체, 타입) : 전달한 객체가 전달한 타입일경우 True, 아니면 False
        if isinstance(other, Student):
            return self.number == other.number # 타입이 맞으면 해당 값이 같은지 비교
        return False


std1 = Student(1, 30)
std2 = Student(1, 50)

total = std1.__add__(std2)
# total = std1 + std2
print(total)
print(std1.__dict__.__getitem__('score'))
print([1, 2, 3].__getitem__(2))
print([1, 2, 3].__contains__(0))
print(std1 == std2)


# 객체끼리의 연산을 할 때 매직매소드로 정의를 하여 해당 값을 받는다.
# DB에서 객체를 가져올땐 가져올 때마다 주소값이 달라져 __eq__을 지정하여 값을 비교