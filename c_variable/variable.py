a = 10; b = 20; c = 30
# 여러 개의 변수를 한 줄로 선언할 때, 세미콜론(;)을 사용하여 한 줄로 작성할 수 있다.

print(a, b, c, sep=', ')

a, b, c = 100, 200, 300
# 파이썬은 상수가 존재하지 않기 때문에 튜플 형식으로 괄호 생략 가능

print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)

temp = a
a = b
# b = a : 이미 a에 33이 저장됐으므로 출력 불가 temp라는 임시저장소에 a를 저장한 후 출력하기
b = temp
print(a, b)

a, b = b, a
print(a, b)

a = 10
print(a, type(a))

a = 10.5
print(a, type(a))

a = 'A'
print(a, type(a))

a = 'ABC'
print(a, type(a))

a = ['A','B','C']
print(a, type(a))

a = {'A':1, 'B':2, 'C':3}
print(a, type(a))

a = 5 > 2
print(a, type(a))

a = True
print(a, type(a))

# 변수명 주의사항
age = 10
print(type(age))

score = 10.5
print(type(score))

grade = 'A'
print(type(grade))

data = "ABC"
print(type(data))

course = ['A', 'B', 'C']
print(type(course))

level = {'A': 1, 'B': 2, 'C': 3}
print(type(level))

condition = True
print(type(condition))

# 서식문자
# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우에 버림을 하여 짝수로 만들어준다.
# 예를 들어 53.45는 53.4로, 32.75는 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest-even)이라고 한다.



name = '박지원'
age = 10
height = 174.45

print("이름 : %s" %name)
print("나이 : %d" %age)
print("키 : %f" %height)
print("키 : %.1f" %height)

print('='*20)
#실습
#정수 2개를 변수에 담기
#두 정수의 합늘 아래 형식을 출력하기
# 1 + 3 = 4
num = 1
number = 3
total = num + number
print("%d + %d = %d " %(num,number,total))


print('='*20)

#format 함수

name = '박지원'
age = 20
height = 156.26

print('이름: {}\n나이: {}\n키: {:.1f}'.format(name, age, height))
print('이름: {0}\n나이: {1}\n키: {2:.1f}'.format(name, age, height))
#방번호 순서를 뜻하는 숫자가 생략되어있음 0,1,2 순서를 바꾸고싶을 떄 바꿀 수 있음
print('이름: {name}\n나이: {age}\n키: {height:.1f}'.format(name=name, age=age, height=height))

print('='*20)

#실습
#아래 메세지를 format 함수를 사용하여 출력한다.
#Hello 파이썬, Python is fantastic !
#Hello 장고, Django is fantastic !
#Hello 리액트, React is fantastic !

# data = "파이썬"
# e_data = "Python"
data, e_data = '파이썬','Python'
# print("Hello {}, {} is fantastic !".format(data, e_data))
name = "장고"
e_name = "Djanggo"
# print("Hello {0}, {1} is fantastic !".format(name, e_name))
mean = "리액트"
e_mean = "React"
# print("Hello {mean}, {e_mean} is fantastic !".format(mean=mean, e_mean=e_mean))


# 자동으로 해당 순서에 값이 반영된다. (코드에 꼭 주석을 다는 연습하기!)
# python_formatting = 'Helllo {}, {} is fantastic !'.format(data, e_data)
python_formatting = f'Helllo {data}, {e_data} is fantastic !'
# 값에 할당된 번호를 작성하면 해당 값이 반영된다.
django_formatting = 'Helllo {0}, {1} is fantastic !'.format(name, e_name)
#값에 이름을 붙이면 해당 이름에 있는 값이 반영된다.
react_formatting = 'Helllo {kor}, {eng} is fantastic !'.format(kor=mean, eng=e_mean)

print(python_formatting,django_formatting,react_formatting, sep='\n')

print('='*20)


#format string
name = '박지원'
age = 20
height = 156.26
# round(실수값, 반올림 자리수)
print(f'이름:{name}')
print(f'나이:{age}살')
print(f'키:{round(height, 1)}')

print('='*20)
#실습
#아래 메세지를 format 함수를 사용하여 출력한다.
#Hello 파이썬, Python is fantastic !
#Hello 장고, Django is fantastic !
#Hello 리액트, React is fantastic !

data = "파이썬"
e_data = "Python"
print(f"Hello {data}, {e_data} is fantastic !")

name = "장고"
e_name = "Djanggo"
print(f"Hello {name}, {e_name} is fantastic !")

mean = "리액트"
e_mean = "React"
print(f"Hello {mean}, {e_mean} is fantastic !")

print('='*20)


#변수를 사용하는 이유 1. 재사용 2. 목적을 자료화