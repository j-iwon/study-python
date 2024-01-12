# unpacking : 값을 풀어서 적는 것
# def get_Total(number1, number2, number3): # 매개변수를 풀어서 적는것
#     return number1 + number2 + number3

# packing : 값을 묶어서 적는 것
def get_total(*numbers):
#     # 외부에서 전달받은 값들이 numbers에 저장된다. 매개변수를 한 번에 받을때는 앞에 *을 붙인다. 이것의 tpye은 tuple이다.
    print(type(numbers))
    total = 0
    for number in numbers:
        total += number

    return total

# packing 상황 1
# 여러개의 값을 콤마로 구분하여 전달한다.
total = get_total(1,2,3,4,5)
print(total)

# packing 상황 2
# 여러개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통채로 들어가게 된다.
# 즉, 결과는 다음과 같다 ([1, 2, 3, 4, 5])
# 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
numbers = [1, 2, 3, 4, 5]
total = get_total(*numbers)
print(total)

# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# packing으로 제작하기
# 성적
def grade_sum(*grades):
    total = 0
    for grade in grades:
        total += grade

    return total
# 이름과 성적
def get_total(name, *scores):
    print(name + '님')
    total = 0
    for score in scores:
        total += score
    return total

print(get_total('한동석', 100, 40, 50))
scores = [100, 40, 50]
print(get_total('한동석', *scores))


# 문자열에서 'A'가 몇 개 있는지 검사하는 함수
# packing으로 제작하기

def get_count_of_A(*strs):
    return[str.count("A") for str in strs]

print(get_count_of_A("AAA","ABC","AVC"))

