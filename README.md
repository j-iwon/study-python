# 1. intro

### Python : 프로그래밍 언어
##### 컴퓨터와 소통하기 위해 사용하는 언어
- ##### 소스코드


    명령어를 작성해 놓은 것
    개발자와 컴퓨터가 소통할 것을 글로 작성해 놓은 것
- ##### 소스파일 


    소스코드가 작성되어 있는 파일
- ##### 컴파일


    사람이 언어를 컴퓨터 언어로 바꿔주는 작업
- ##### 컴파일러


    컴파일 해주는 프로그램 또는 명령어

- ##### 인터프리터


    인터프리트를 해주는 프로그램 또는 명령어
　
###### ※ 정의 ※

    파이썬은 인터프리터 안에 컴파일러를 내장하고 있다.
    인터프리터는 매번 소스코드를 한 줄 씩 해석해서 실행하므로(개별처리),
    이 작업으로 인해 전체 프로그램의 퍼포먼스에 큰 손해를 본다.
    파이썬은 소스코드를 바이트 코드로 컴파일한 뒤
    이를 번역기가 돌려주는 방식으로 실행된다.
    따라서 컴파일 언어니지, 인터프리터 언어인지를 구분하는 것이 아니라
    어떻게 구현하였는지로 판단해야 한다.

### 프로그램

    소스코드로 잘 짜여진 틀

##### 1. 일반 프로그램

    
    - 프로그램
    - OS(운영체제) : 하드웨어에 적절한 전기신호를 흘려주는 역할.
    - 하드웨어

    일반 프로그램은 이식성이 좋지 않다.

#####   2. Python 프로그램

    - 프로그램
    - PVM : Python 프로그램을 OS에 맞게 번역한다. (파이썬 버츄얼 머신(=운영체제)) 힙 메모리
    - OS(운영체제) : 하드웨어에 적절한 전기신호를 흘려주는 역할.
    - 하드웨어

    Python 프로그램은 이식성이 좋다.

- ##### 콘솔


    개발자가 내 컴퓨터(로컬)와 직접 소통할 수 있는 입출력장치(입력:키보드, 출력:모니터)

- ##### 터미널


    내 컴퓨터(로컬)뿐만 아니라 다른 컴퓨터에 원격으로도 접속할 수 있는 콘솔을 구현한 프로그램

- ##### 쉘


    명령어 해석기

###### ※ 정리 ※

    1. 개발자가 터미널에 명령어 입력
    2. 쉘이 명령어를 받은 뒤 해석 및 수행
    3. 터미널은 쉘에게 받은 결과를 화면에 출력

# variable

- ##### 변수
    ##### 변수는 값을 담는 저장공간이다.


    x = 10, x라는 이름의 저장공간이 RAM(메모리)에 만들어지고 10이라는 값이 들어간다.
    - = 대입연산자, 우를 좌에 대입한다.
    - Python은 순수객체지양언어로 class 언어 사용
    - 코드를 보고 선언인지 사용인지 구분할 줄 알아야 한다. 대입연산자가 있으면 선언, 없으면 사용

- ##### 자료형(Type): 저장공간의 종류
    ##### 동적 바인딩으로, 값에 따라 자료형이 정해진다.


    자료형(type)       값
    정수(int)       0, 10, -187, ...
    실수(float)       0.0, 10.58, -77.568, ...
    문자열(str)       '0', "0.0", """한동석""", '''Python''', ...
    리스트(list)       [1, 2, 3], [0], [3,], ...
    튜플(tuple)       (1, 2), (), 1, 2, 3, (1,), ...
    딕셔너리(dict)   {key:value,}, ...
    집합(set)       {1, 2, 3}, {1}, ...
    불린(bool)       True, False

##### 변수명 주의사항

    문자로 시작해야 한다.
    특수문자는 사용할 수 없다. 단, _는 허용한다.
    소문자로 시작한다.
    공백을 사용할 수 없다.
    되도록 한글은 사용하지 않는다.
    명사로 사용한다.
    뜻이 있는 단어를 사용한다.
        - a, b, c, d, e, ... (X)
        - data, number, age, name, ...(O)

- ##### 변수의 선언과 사용


    1. 선언 : 대입연산자가 있다면 선언이다, 값으로 봐서는 안된다!
    2. 사용 : 대입연산자가 없다면 사용이다, 반드시 값으로 봐야한다.

- ##### 표기법 (Python에서 사용 : *)


    - 파스칼 표기법(클래스명, 오류명)
        대문자로 시작하고 이어지는 단어의 시작은 대문자로 작성한다.
        PascalCase

    - 카멜 표기법(Java등에서 사용)
        소문자로 시작하고 이어지는 단어의 시작은 대문자로 작성한다.
        cameCase

    - 스네이크 표기법(변수,함수)
        snake_case

    - 케밥 표기법(HTML,CSS,URL 등에서 사용)
        kebab-case

- ##### 서식문자 
    ##### 따옴표 안에서 변수 또는 값을 사용해야 할 때 작성한다.
    ##### 반드시 따옴표 안에서 작성한다


    ----------------------------------
    서식문자   설명
    ----------------------------------
    %d           10진수 정수 표현
    %f           실수 표현
    %s           문자열 표현
    ----------------------------------

- ##### 변수를 사용하는 이유


    1. 반복되는 값을 쉽게 관리하고자 할 때
    2. 값에 의미 부여를 할 때 (자료구조)

- ##### 알고리즘과 자료구조


    1. 알고리즘이란, 문제가 발생했을 때 해결할 수 있는 절차
        예) 3과 1을 더해서 결과를 출력하시오. 라는 문제가 생겼을 때
            문제를 해결하기 위한 순서를 짜는것.
            1) 두 정수를 담을 변수 선언
            2) 두 정수의 합을 담을 변수 선언
            3) 형식에 맞게 작성한 문자열 값을 담을 변수 선언
            4) 형식을 출력

    2. 자료구조란, 의미 없는 값을 하나의 정보로 변환하고 이는 저장공간의 종류를 의미한다.
        예) 3개의 정수가 있을 때, 이를 빠르게 가져오는 서비스를 제작해야한다.
            빠르게 가져올 떄에는 list에 담아주는 것이 효과적이다.

- ##### 형변환


    bin(), oct(), hex(), int(), float(), str(), bool()

# 2. operator

- ##### 연산자
    ##### 기능이 있는 특수문자


    1. 산술 연산자

        ----------------------------------
        연산자   예시   설명
        ----------------------------------
        +       3 + 5   더하기
        -       3 - 5   빼기
        *       3 * 5   곱하기
        /       3 / 5   나누기
        **       3 ** 5   제곱
        //       3 // 5   몫
        %       3 % 5   나머지
        ----------------------------------
　

    2. 대입(allocation) 연산자

        -------------------------------------------
        연산자   예시           설명
        -------------------------------------------
        =       data = 10       좌항에 우항을 대입
        +=       data += 10       data = data + 10
        -=       data -= 10       data = data - 10
        *=       data *= 10       data = data * 10
        /=       data /= 10       data = data / 10
        **=       data **= 10       data = data ** 10
        //=       data //= 10       data = data // 10
        -------------------------------------------
　

    3. 비교 연산자 # 중요

        ※ 조건식 - 참 또는 거짓, 둘 중 하나가 나오는 식
        ※ 조건식은 항상 값으로 본다(True 또는 False)

        ----------------------------------------------------------------
        연산자   예시                   설명
        ----------------------------------------------------------------
        ==       data == 10               같으면 True, 같지 않으면 False
        !=, <>   data != 10, data <> 10   같지 않으면 True, 같으면 False
        >       3 > 5                   보다 크다
        <       3 < 5                   보다 작다
        >=       3 >= 5                   이상
        <=       3 <= 5                   이하
        ----------------------------------------------------------------
　

    4. 논리 연산자

        ----------------------------------------------------------------
        연산자   예시               설명
        ----------------------------------------------------------------
        and       a == b and c == d   조건식 둘 다 True일 경우 True
        or       a == b or c == d   조건식 둘 중 하나라도 True일 경우 True
        not       not (a == b)       True를 False로 False를 True로 변경
        ----------------------------------------------------------------
　

    5. 멤버 연산자

        -----------------------------------------------------------------------------------------------------
        연산자   예시                                   설명
        -----------------------------------------------------------------------------------------------------
        in       "a" in "abc", 2 in [1, 2, 3]           좌항이 우항에 포함되었다면 True 아니면 False
        not in   "a" not in "abc", 2 not in [1, 2, 3]   좌항이 우항에 포함되어 있지 않다면 True 포함되면 False
        -----------------------------------------------------------------------------------------------------
　

    6. 식별 연산자

        -----------------------------------------------------------------------------------------------------
        연산자   예시                                       설명
        -----------------------------------------------------------------------------------------------------
        is       a = 10; b = a; a is b                       두 객체 모두 같은 주소일 경우 True 아니면 False
        is not   a = [1, 2, 3]; b = [1, 2, 3]; a is not b   두 객체 모두 같은 주소일 경우 True 아니면 False
        -----------------------------------------------------------------------------------------------------

# 3. input

- ##### 입력 상태


    커서가 깜박이고 있는 상태를 의미.
    항상 입력 전에 출력을 해서 사용자가 정확한 값을 입력할 수 있도록 한다.

- ##### 입력 함수


    콘솔에서 입력을 받아야 할 때 사용하며, 입력받은 값은 문자열 값으로 리턴된다.
    커서를 깜박여서 입력 상태에 돌입한다.

    input("출력할 메세지")

# 4. control_statement
    
- ##### 제어문


    컴파일러의 방향을 제어할 수 있는 문법이며,
    건너뛰기, 되돌아가기 등이 있다.

- ##### 조건문
##### if문

    1.
        if 조건식:
            실행할 문장
        if 조건식:         #위의 조건의 결과와 상관없이 실행
            실행할 문장
        if 조건식:
            실행할 문장
        ...

    2.
        if 조건식:
            실행할 문장
        elif 조건식:       #위의 조건이 True면 실행 x
            실행할 문장
        ...
        else:             #조건식이 없음 위의 조건이 다 F라는 전제
            실행할 문장

- ##### 반복문
##### for : in절 뒤의 요소를 순서대로 변수에 담고 다음 값이 더 이상 없을 경우 종료
                                #포함          #제외       #증가량
        for 변수명 in range(inclusive_start, exclusive_end, step):
            실행할 문장

##### while : 조건식이 True일 때 반복, False일 때 종료                         # 몇 번 출력해야할지 모를때

        whlie 조건식:
            실행할 문장

# 5. collection
## 1) list
            
- ##### list


    - 여러 개의 저장공간이 나열되어 있는 것.                              
        참조연산자 <- 값을 읽어온다.
        (l+2) -> ㅣ[2] -> ㅣ=[1,2,3] 로 간편하게 씀

    - 사용 목적
        1) 여러 번 선언하지 않고 한 번만 선언하기 위해서 사용
        2) 규칙성 없는 값에 규칙성을 부여하기 위해 사용

- ##### list 선언


    - 어떤 값을 넣을 지 알 때
        list명 = [값1, 값2, ...]

    - 어떤 값인 지는 모르지만, 칸 수는 알 때
        list명 = [값] * 칸수

    - 어떤 값인지도 모르고, 칸 수도 모를 때
        listaud = []
　

    list명 = [값1, 값2, ...]                                    
            직접 입력 : 어떤 값을 넣을지 미리 알고있는 경우

    list명 = [값]* 칸수                                         
            어떤 값을 넣을지는 모르지만 몇 개를 넣을지 알고있을때 ex) [0] * 10

    list명 = []                                                
            몇 칸을 넣을지도 모를 경우 만든 다음 밑에서 작성

    list명 = list(range(start, end, step)                      
            함수 넣기 처음부터 규칙성 있는 값을 넣을 때


- ##### list 길이


    len(list명)                                                
    값이 변경되어도 len이 알아서 계산해줌

- ##### list 사용


    data_list = [1,2,3]

    - 값 넣기
        (추가)
            list명.append(값)
            data_list.append(4)
            결과 : [1, 2, 3, 4]

        (삽입)
            list명.insert(인덱스번호, 값) #내가 원하는 위치에 넣을 수 있음. 값과 함께 어디에 넣을지 지정해줌.
            data_list.insert(1, 1.5)
            결과 : [1, 1.5, 2, 3]


    - 값 삭제
        list명.remove(값)
            중복시 먼저 나온 값(낮은 인덱스 값)이 삭제
        del(list명[인덱스])
        del list명[인덱스]
            인덱스로 삭제                           # 중복된 값이 있어도 원하는 곳의 값을 삭제할 수 있음. 값만 입력하면 여러 값중 항상 첫번째 값이 지워짐.

        list명.clear()
            모든 값 삭제


    - 값 검색
        list명.index(값)
            값이 들어있는 저장공간의 인덱스 번호
            중복 시 먼저 나온 값의 인덱스 번호         # if문 count로 검색


    - 값 수정
        list명[인덱스] = 새로운 값

## 2) dict

- ##### dict


    - 한 쌍으로 저장되어 관리한다. ※ 기존의 자료구조와 다른 점
    - len()를 사용하면 한 쌍을 1로 카운트 한다.
    - 키 값은 중복이 될 수 없지만 값은 중복이 가능하다.
    - 키 값을 주면 그 키의 값(벨류)을 가지고 온다.

    list 키값-> index(번호)
    dict 키값-> name(이름)

- ##### dict 선언


    dict명 = {키: 값, 키: 값, ...}

- ##### dict 사용


    - 추가, 수정
        (키값은 수정이 안되기 때문에 추가와 수정 명령어가 같다. 미리 검사를 한 후 명령하기)
        dict[키] = 값
        키 값이 기존에 있으면 수정이고, 기존에 없으면 추가이다.

    - 삭제
        del dict명[키]

    - 검사
        키 in dict명: 키가 있으면 참
        키 not in dict명: 키가 없으면 참

# 6. function        

- ##### 함수
    ##### 이름 뒤에 소괄호, 작성된 코드의 주소값을 담고 있는 저장공간


    f       (x)         = 2x+1
    함수명   매개변수        리턴값

- ##### 함수 선언


    def 함수명(매개변수, ...):
        실행할 문장
        return 리턴값

    - def가 있으면 선언, 없으면 사용

- ##### 함수 사용


    함수명(값1, ...)

- ##### 함수를 사용하는 목적


    1. 재사용
        ※절대 특정성을 부여해서는 안된다.

    2. 간결화

- ##### 함수 선언 순서


    문제) 두 정수의 덧셈을 해주는 함수 구현

    1. 함수명을 생각한다.
       def add():

    2. 매개변수를 생각한다. # 받아올 것을 생각해야한다. 필요한 것 두 정수 !
       def add(number1, number2):

    3. 실행할 문장을 생각한다.
       def add(number1, number2):
            result = number1 + number2 # 출력하라고 하면 print()

    4. 리턴 값을 생각한다.
        def add(number1, number2):
            result = number1 + number2
            return result


- ##### 매개변수 선언 방법


    1. packing(args)
        여러 개의 값을 마구잡이로 받을 때 사용한다

    2. kwargs
        여러 개의 값을 key=value 형식으로 받는다.

    3. unpacking
        매개변수에 *로 시작하면 kwargs 형식과 동일하게 받아야 하고,
        그냥 매개변수가 나열되어 있으면, 값만 전달해도 된다.


- ##### packing(args) 함수 사용 방법


    1. 여러 개의 값을 콤마로 구분하여 전달
    2. 여러 개의 값을 묶은 뒤, 앞에 *을 작성하여 전달

- ##### kwargs 함수 사용 방법


    1. 여러 개의 값을 콤마로 구분하여, key=value 형태로 전달
    2. dict에 정보를 담은 뒤 **을 붙여서 전달

# 7. closure    

- ##### 클로저(closure, 폐쇄)
    ##### 함수 안에 함수, 모듈화


    - 함수가 정의된 시점의 변수(지역변수)를 기억하고, 이 변수를 나중에 참조 혹은 가능하도록 해준다. 
    - 지역변수가 메모리상 전역변수와 다를게 없어짐.
    - 내부 영역에 선언된 변수(지역변수)는 외부에서 접근이 불가능하기 때문에 데이터 은닉을 할 수 있으며, #은닉화, 캡슐화라고 한다.
    - 함수가 종료된 이후에도 지역변수에 접근할 수 있기 때문에 데이터 지속성을 가지고 있다.
    - 또한 다른 함수를 인자로 받거나 리턴할 수 있는 함수형 프로그래밍이 가능해진다. # 함수를 값처럼 쓸 수 있다.
    - 하지만 코드 복잡성이 증가하고 지역변수를 메모리에 유지하기 때문에 메모리 사용량이 증가될 수 있다.

- ##### 클로저 구현 코드


    def out(arg):
        local_variable = value #지역변수 선언

        def in(arg):
            #read local_variable #지역변수 선언한것을 가져다 쓸 수 있음
            value = operate somthing

            return value

        return in # in함수를 out 함수에서도 사용할 수 있도록 return 해줘야한다

# 8. decorator

- ##### 데코레이터(장식)


    좋은 개발 환경에서는 개발자가 메인 로직(비즈니스 로직)에만 집중할 수 있게 한다.
    보안이나 로그, 트랜직션, 예외처리와 같이 비즈니스 로직은 아니지만,
    반드시 처리가 필요한 부분을 주변 로직이라고 한다.
    주변 로직을 다른 함수에 분리시켜놓은 뒤 메인 로직이 실행될 때 함꼐 실행되도록 할 수 있다.

- ##### 데코레이터 동작 코드


    방식 1.
    def 데코레이터 이름(원래 함수): # 함수는 값이기 때문에 매개변수로 받아올 수 있다.
        def 주변 로직 함수(원래 함수의 매개변수):
            완성 코드 = 주변 로직 # 매개변수를 받았으니 출력
            원래 함수(완성 코드) # 사용

        return 주변 로직 함수

    방식 2.
    def 데코레이터 이름(원래 함수): 
        def 주변 로직 함수(원래 함수의 매개변수):
            주변 로직 # 출력을 하거나 다른 함수를 입력
            원래 함수(원래 함수의 매개변수)

        return 주변 로직 함수

# 9. class
##### 클래스(class) : 반
##### 공통 요소를 한 번만 선언하자!

    1. 타입이다.
        클래스 안에 선언된 변수와 메소드를 사용하고 싶다면,
        해당 클래스 타입으로 변수를 선언해야 한다.
        - 클래스 안에 선언된건 함수(X) 메소드(O)

    2. 주어이다.
        원숭이가 바나나를 먹는다.
        원숭이(주어)가 바나나(목적어)를 먹는다(동사).
        Monkey.eat("바나나")

##### class 선언

    class 클래스명:
        필드(변수, 메소드)  

    - 클래스 안에 선언되는 모든 것을 필드라고 부른다.

##### class의 필드를 사용
    1. 객체화(instance)             
        - 클래스는 객체로 접근해야한다. 이를 객체화 시킨다고 한다.
        객체(instance variable)를 만드는 작업.
        추상적인 개념을 구체화시키는 작업 #ex) 자동차 -> 엄마차

    2.생성자
        클래스 이름 뒤에 소괄호가 있는 형태, 메소드와 기능이 똑같지만 메소드라고 부르지 않는다.
        생성자는 할당한 필드의 주소를 자동으로 리턴하기 때문에,
        선언 시, 리턴이라는 기능을 사용할 수 없다.

    3.기본 생성자
        매개변수가 없는 생성자를 뜻하며, 클래스 선언 시 자동으로 선언된다.
        사용자가 직접 생성자를 선언하게 되면 자동으로 선언되지 않는다.

    4.self
        필드에 접근한 객체가 누구인지 알아야 해당 필드에 접근할 수 있다.
        이 때 접근한 객체가 가지고 있는 필드의 주소값이 self라는 변수에 자동으로 담긴다.

# 10. inheritance

- ##### 상속


    1. 기존에 선언된 클래스의 필드를, 새롭게 만들 클래스의 필드로 사용하고자 할 때
    2. 여러 클래스를 선언하면서, 겹치는 필드가 있을 경우 부모 클래스를 선언한 뒤
       겹치는 필드를 구성하고 각 자식 클래스에 상속해준다(추상화).

- ##### 상속 문법


    class A:
        A 필드

    class B(A):
        A, B 필드

    A: 부모 클래스, 상위 클래스, 슈퍼 클래스, 기반 클래스
    B: 자식 클래스, 하위 클래스, 서브 클래스, 파생 클래스

- ##### super().__init__(): 부모 생성자


    자식 (클래스 타입의) 객체로 부모 필드에 접근할 수 있다.
    하지만 자식 생성자만 호출하기 때문에, 자식 필드만 메모리에 할당된다고 생각할 수 있다.

    사실, 자식 생성자에는 항상 부모 생성자를 호출하기 때문에, 자식 생성자 호출 시 부모와 자식 필드 모두 메모리에 할당된다.
    이 때 부모 생성자를 호출하는 방법은 super().__init__()를 사용하는 것이다.
    만약, super().__init__()을 직접 작성하지 않더라도 컴파일러가 자동으로 작성해준다.

    - 모든 class 는 object를 상속받는다.

- ##### 오버라이딩(재정의, 무시하기)


    부모 필드에서 선언한 메소드를 자식 필드에서 수정하고자 할 때 재정의를 해야한다.
    이는 자식에서 부모 필드의 메소드와 동일한 이름으로 선언하는 문법을 의미한다.
    접근한 객체와 가까운 곳부터 찾기 때문에, 자식 필드에 해당 메소드가 있다면 재정의된 메소드가 실행된다.

# 11. magic method

- ##### 매직 메소드


    클래스 안에 정의할 수 있는 스페셜 메소드이다.


    연산자     메소드                         설명
    ───────────────────────────────────────────────────────
     +      __add__(self, other)            덧셈
     *      __mul__(self, other)            곱셈
     -      __sub__(self, other)            뺄셈
     /      __truediv__(self, other)        나눗셈
     //     __floordiv__(self, other)       몫
     %       __mod__(self, other)           나머지
     **      __pow__(self, other[, modulo]) 제곱
     >>      __lshift__(self, other)        우쉬프트
     <<      __rshift__(self, other)        좌쉬프트
     &       __and__(self, other)           논리곱
     ^      __xor__(self, other)            배타논리합
     |      __or__(self, other)             논리합
    +=      __iadd__(self, other)           누적 더하기
    -=      __isub__(self, other)           누적 빼기
    *=      __imul__(self, other)           누적 곱하기
    /=      __idiv__(self, other)           누적 나누기
    //=     __ifloordiv__(self, other)      누적 몫
    %=      __imod__(self, other)           누적 나머지
    **=     __ipow__(self, other)           누적 제곱
    >>=     __irshift__(self, other)        누적 우쉬프트
    <<=     __ilshift__(self, other)        누적 좌쉬프트
    &=      __iand__(self, other)           누적 논리합
    ^=      __ixor__(self, other)           누적 배타논리합
    |=      __ior__(self, other)            누적 논리합
     <      __lt__(self, other)             작다(미만)
     <=     __le__(self, other)             작거나 같다(이하)
     ==     __eq__(self, other)             같다
     !=     __ne__(self, other)             같지 않다
     >      __gt__(self, other)             크다(초과)
     >=     __ge__(self, other)             크거나 같다(이상)
     [i]    __getitem__(self, index)        인덱스 연산자
     in     __contains__(self, value)       멤버 확인
     len    __len__(self)                   요소 길이
     str    __str__(self)                   문자열 표현
    
            __init__                       생성자
            __del__                        소멸자
            __new__                        할당자
            __repr__(self)                 __str__을 정의하지 않을 경우, __repr__이 대신 쓰인다
                                           객체를 표현(객체의 주소)하는 목적으로 사용한다

# 12. module

- ##### 모듈(부품)


    변수와 함수, 클래스 등을 모아 놓은 파이썬 파일

- ##### 모듈 사용


    import [모듈명]
    사용할 함수의 소속을 직접 코드에 작성하고 모든 필드를 사용하고자 할 때

    import [모듈명] as [사용할 이름]
    모듈명이 길거나 복잡할 때 원하는 이름으로 설정해서 사용

    from [모듈명] import [필드명,...]
    모듈명을 직접 코드에 작성하지 않고 필드를 바로 사용하고자 할 때

    from [모듈명] import *
    모듈 안에 있는 모든 필드를 바로 사용하고자 할 때

- ##### 패키지


    - 폴더를 생성하여 .py또는 .ipynb파일을 관리하고자 할 때 해당 폴더를 패키지라고 한다.
    - __init__.py 파일을 생성해야 패키지로 인식되지만, 상위 버전(3.3 부터)에서는
    - __init__.py 파일이 없어도 패키지로 인식된다.
    - 하지만, 하위 버전(3.3 미만)에서도 인식되기 위해서는 직접 생성해 놓는 것이 좋다.
　

    ※ 주의사항
    모듈을 사용할 파일의 이름이 모듈과 같으면 절대 못쓴다.

# 13. api

- ### API(Application Programming Interface)


    선배 개발자들이 미리 작성해놓은 틀(소스코드)
　

    1. 내부 API(기본 API)
        python 설치 시 다운로드 되었던 모듈.
        바로 사용할 수 있는 API.

    2. 외부 API
        해당 기업에서 배포한 코드를 다운로드 받은 뒤 사용할 수 있는 모듈.
        기본으로 제공되지 않는 API.

# 14. exception

- ##### 예외 처리


    프로그램 실행 중 오류 발생 시 강제 종료되기 때문에 이를 막기 위하여 예외 처리를 작성한다.
    제어문으로 오류를 막을 수 없는 상황에서는 반드시 예외처리를 작성해야 한다.

- ##### try, except 문


    1.
        try:
            오류가 발생할 수 있는 문장

        except 발생오류 as 오류객체: #발생오류 = class 를 객체화(필드가 메모리에 올라갔다, 주소값이 생긴다) 주소값을 담을 곳을 만들면 오류X, 없으면 오류O
            오류 발생 시 실행할 문장

        ...

    2.
        try:
            오류가 발생할 수 있는 문장

        except 발생오류:
            오류 발생 시 실행할 문장

        ...

    3.
        try:
            오류가 발생할 수 있는 문장

        except:
            오류 발생 시 실행할 문장

        ...

        finally: #모든 상황에서 실행됨
            오류 발생 여부와 상관없이 실행

- ##### 예외 발생시키기


    심각한 문제가 발생하기 전에 일부러 프로그램을 강제 종료할 때 사용한다.
    예외를 한 곳에서 묶어서 처리하기 위해 사용한다(상위 과정에서 다룰 예정)


    raise 발생오류

- ##### 예외 만들기


    class 오류명(Excrption):
        def __str__(self):
            return "오류 메세지"

# 15. file

- ##### 파일


    외부에 파일을 생성하거나 내용을 작성할 수 있으며, 기존의 내용도 읽어올 수 있다.

- ##### 파일 생성하기


    파일을 열고 작성할 때 사용한다.
    'w'를 작성하서 운영체제에게 파일을 여는 목적을 알려줘야 하며, 이 때 'w'를 작성한다.
    open(path, 'w')

- ##### 내용 추가하기


    기존의 내용을 없애지 않고, 아래에 내용을 추가한다.
    이 때에는 추가 모드인 'a'를 작성한다.
    open(path, 'a')

- ##### 파일 읽기


    기존 내용을 한 줄씩 읽어올 때 'r'를 작성하여 읽기 모드로 파일을 열어준다.
    open(path, 'r')

# 16. generator

- ##### 제너레이터(Generator)


    한 번에 하나씩 구성요소를 반환해주는 객체
    대용량 데이터 및 많은 반복이 필요한 코드에서 메모리를 적게 사용할 수 있는 고성능 방법
    필요할 때마다 하나씩 가져오기 때문에 무거운 객체를 다룰 때 사용한다.
　


    list comprehension
        [operate for variable in range(end)]
    
    generator expression
        (operate for variable in range(end))




