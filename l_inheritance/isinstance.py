class A:
    pass


class B(A):
    pass


a = A()
b = B()

print(isinstance(a, A))
print(isinstance(b, B))
# 모든 자식은 부모 타입 이다. 결과 : True
print(isinstance(b, A))
# 부모는 절대 자식 타입이 될 수 없다. 결과 : False
print(isinstance(a, B))