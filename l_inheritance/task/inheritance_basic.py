# 인간(부모)
# 이름, 나이
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 걷기(walk)
# '두 바로 걷습니다' 출력
    def walk(self):
        print('두 발로 걷습니다.')

person = Person('인간',20)
person.walk()

# 원숭이(자식)
# 이름, 나이, 동물원 이름
class Monkey(Person):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo
# 걷기(walk)
# '두 발로 걷습니다', '네 발로 걷습니다' 출력
    def walk(self):
        super().walk()
        print('네 발로 걷습니다.')

monkey = Monkey('킹콩', 8,'에버랜드')
monkey.walk()