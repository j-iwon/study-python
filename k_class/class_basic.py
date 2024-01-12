# 동물
# 이름, 나이, 성별, 음식 개수, 체력 개수
# 먹기, 산책하기

class Animal: #class명 앞글자는 대문자로

    def __init__(self, name, age, gender, feed_count=1, life=1): #필수로 입력해야할 것을 앞으로 빼고, 나머지는 뒤로 num=1
        self.name = name
        self.age = age
        self.gender = gender
        self.feed_count = feed_count
        self.life = life

    # 음식 1개 소모, 체력 1개 획득
    def eat(self): #무조건 자동으로 들어오게 하기 위해 빈칸이 아닌 self 반드시 입력
        self.feed_count -= 1
        self.life += 1
        # pass

    # 체력 1개 소모, 음식 1개 획득
    def walk(self):
        self.life -= 1
        self.feed_count += 1
        # pass

tiger = Animal(name='호랑이', age=10, gender='수컷')
lion = Animal(name='사자', age=20, gender='암컷')

tiger.eat()
lion.walk()

print(tiger.name, tiger.age, tiger.gender, tiger.feed_count, tiger.life) # . 앞이 객체
print(lion.name, lion.age, lion.gender, lion.feed_count, lion.life)


