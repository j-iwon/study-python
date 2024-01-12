def set_key(key):
    formatting = ''

    # 클로저
    def set_value(value):
        nonlocal formatting
        formatting = f'{key}:{value}' # 위에서 받은 key와 value를 모두 사용하여 새롭게 선언
        return formatting

    return set_value
# set_value 에서 formatting 을 선언했기 때문에, set_key를 사용하는 순간 값이 set_value가 되어야함
set_name = set_key('이름') #set_key()괄호가 붙어 함수임을 볼 수 있어야함
formatting = set_name("한동석")
print(formatting)
# set_key()() < 라고 선언하면 set_value의 값이 된다.

# key값이 없이는 value를 실행할 수 없다.
# read가 아니라 right 하는 경우 : nonlocal 선언(set_value의 지역변수가 아니라고 선언) 후 사용할 수 있다.

# '나이: 00살'

set_age = set_key('나이')
formatting_age = set_age('00살')
print(formatting_age)

# 실습 1
# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

# ((Hint))
# def set_topic(**kwargs):
#     if 'name' in kwargs:
#        pass
#     else:
#        pass
#     return formatting


def set_topic(**kwarge):
    result = 0
    if 'name' in kwarge:
            def set_name(sep=', '):
                formatting = f'name{sep}{kwarge.get("name")}'
                return formatting
            result = set_name
    else:
            def set_not_name(sep=', '):
                formatting = f'{kwarge.get("topic")}{sep}{kwarge.get("point")}'
                return formatting
            result = set_not_name

    return result

print(set_topic(name='한동석')(': '))
print(set_topic(topic='지구 온난화',point='오존층 파괴를 막기 위해 인간이 해야할 일')("\n"))

# 실습 2
# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

# ((Hint))
# def set_product(*args):
#     pass

# 상품정보 (상품명, 가격)을 전달받은 *args 는 tuple type 이고 [{}:{}] 일것이라 생각하고 시작한다.
# **kwargs = 외부에서 받아올 새로운 정보를 받아온다. 함수 1,2,3 에 사용
# 어떻게 함수를 골라쓸 것인가? return으로 3개의 함수를 전달해야한다.
# return { 'insert':insert, 'update':update, 'select_all':select_all } 딕셔너리로 전달해야 사용자가 정확하게 골라쓸 수 있다.
# set_product(*products) <- *을 붙이는 이유? {},{}를 풀어서 써도 되지만 한꺼번에 쓸 때에 각각 들어가게 하기 위해서
# 딕셔너리와 함수를 구분

def set_product(*args):
    number = 0

    for product in args:
        number += 1
        product['number'] = number

    def insert(**kwargs):
        nonlocal number, args
        number += 1
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                break

    def select_all():
        return args

    return {'insert': insert, 'update': update, 'select_all': select_all}


products = [
    {'name': '마우스', 'price': 5000},
    {'name': '키보드', 'price': 25000}
]

product_service = set_product(*products)
print(products)
product_service.get('insert')(name='모니터', price=80000)
print(product_service.get('select_all')())
product_service.get('update')(name='키보드', price=20000, number=2)
print(product_service.get('select_all')())