class Car:

    # 정적 변수(static variable)
    wheel = 4 # 객체화 전 static에 바로 선언되는 변수는 모든 객체가 공유하는 변수(값)이다. 수정시 필드(객체)에 접근할 필요 없이 class로 바로 접근.

    def __init__(self, brand='', color='',price=0): #필드를 메모리에 올리는 역할 = 생성자
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_stop(self):
        print(self.brand + '시동 꺼짐')


# mom_car = Car('Benz', 'Black', 15000)
# daddy_car = Car('BMW', 'Blue',8800)
#
# mom_car.engine_start()
# daddy_car.engine_start()
#
# print(Car.wheel)
#
# Car.wheel = 6 # Class로 바로 접근
# print(Car.wheel)

cars = [Car, Car] #클래스명만 입력해도 주소값이 할당됨 Car라는 자료형을 미리 선언해놓음
mom_car = cars[0]() #소괄호를 하면 선언해놓은 주소값에 메모리가 할당됨(생성자가 완성됨). 호출할 때 반드시 소괄호 !
daddy_car = cars[1]()
print(mom_car, daddy_car, sep='\n')