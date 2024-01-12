user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]


# 추가(초보자용)
# def insert(*, number, name):
#     '''
#
#     :param number: 회원 번호
#     :param name: 회원 이름
#     '''
#     user_info.append({'number': number, 'name': name})


# 추가
# 회원 번호는 자동 증가한다.
number = 5
def insert(name):
    global number
    number += 1
    user_info.append({'number': number, 'name': name})


# 목록
def select_all():
    return user_info


# 조회(번호로 조회)
def select(number):
    for user in user_info:
        if user['number'] == number:
            return user
    return {}


# 수정(번호로 이름 수정)
def update(**kwargs):
    '''

    :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
    '''
    select(kwargs.get('number'))['name'] = kwargs.get('name')


# 삭제(번호로 삭제)
def delete(number):
    del user_info[user_info.index(select(number))]

# -----------------------------------------------------------
user_info = [] #수정
user_info.append({'number': 6, 'name': ''}) #사용
# -----------------------------------------------------------


post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]
# 전역 변수
number = 5
# 추가(조회수는 전달받지 않고 기본값 0으로 설정)

def insert(*,title,content,file,read_count=0):
    global number
    number += 1
    post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})

insert(title='테스트 제목6', content='테스트 내용6', file='/usr/post/file/img006.png')
print(post_info)

# 목록(최신순으로 조회)
def select_all():
    return post_info[::-1]

print(select_all())


# 조회(번호로 조회, 조회수 1 증가)
def read(number):
    post = select(number)
    post['read_count'] += 1
    return post
def select(number):
    for post in post_info:
        if post['number'] == number:
            return post
    return {}

result = read(2)
print(result)

# 수정(번호로 정보 수정)
def update(**kwargs):
    post = select(kwargs.get('number'))
    post['title'] = kwargs.get('title')
    post['content'] = kwargs.get('content')
    post['file'] = kwargs.get('file')


# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]

result = delete(1)
print(post_info)