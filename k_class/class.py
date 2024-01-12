class A:

    #기본 생성자 생략 (주소값을 self로 지정하고 메모리에 필드를 할당하는건 __new__ , 실질적으로 원하는걸 받아서 데이터를 생성하는건 __init__)
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, data1, data2, name=''):
        print('__init__')
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name

    def print_name(self):
        print(self.name)

# # a가 객체, A는 클래스, A()는 생성
# a = A() # a로 객체화를 하고
# print(a)
# a.data1 = 10 # a라는 필드에 data1이라는 주소값을 할당하여 10이라는 값을 넣음
# print(a.data1)
# a.print_name('a')
#
# b = A()
# print(b)
# b.data1 = 10
# print(b.data1)
# b.print_name('b')

# a = A()
a = A(10, 20, 'a')
print(a)
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

# b = A()
b = A(100, 200, 'b')
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()