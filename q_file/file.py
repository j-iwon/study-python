# 절대 경로 : 대한민국 서울시 강남구 역삼동 123-123 103동 203호
# 어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
# C:/a/b, D:/User/ted, ..

# 상대 경로 : 직진해서 좌회전 후 오른쪽 건물 (어디에 있는지에 따라 도착지가 달라짐)
# 현재 위치에 따라 변경되는 경로
# ./ : 현재 경로, ../ : 이전 경로, ./src/images, ../../a/b, src/images

# 파일 생성하기
# file = open('food.txt','w', encoding='UTF-8')
# file.write('부대찌개\n')
# file.write('햄버거\n')
# file.close()

# 파일 추가하기
# file = open("food.txt", "a", encoding="UTF-8")
# file.write('피자\n')
# file.close()

# 파일 읽기 ※중요※
# try:
#     file = open("food.txt", "r", encoding="UTF-8")
#     # print(file.readlines()) #List로 return
#     for i in range(4):
#         # print(file.readline(), end='') #비어있는 문자열이 return
#
#         print(i + 1)
#         if file.readline() == ''
#             print('다 읽었어요!')
#
#
#     print(file)
# except FileNotFoundError:
#     print('경로를 다시 확인해주세요')


# with 문을 사용하면, 자동으로 file이 close 된다
# 처음에 enter가 시작되고 마지막에 exit 문이 실행되는데 exit 에서 close를 해주기 때문이다.
# with NameCard() as name_card:
#     name_card.print_info('한동석')


# 수정

# 외부 파일에 있는 내용을 담아줄 변수
content = ""
with open('food.txt', 'r', encoding='utf-8') as file:
    line = None
    # 전체 내용을 한 줄씩 읽어오기
    while line != '':
        # 한 줄을 line에 담기
        line = file.readline()
        # 담은 내용이 찾고 있는 햄버거일 경우
        if line == '햄버거\n':
            # content에 치킨으로 변경해서 담기
            content += '치킨\n'
            continue

        # 수정 대상이 아닌 줄은 그대로 content에 담기
        content += line

    # 수정 완료된 문자열 값 확인
    print(content)

# 기존의 내용을 수정 완료된 문자열로 덮어쓰기
with open('food.txt', 'w', encoding='utf-8') as file:
    file.write(content)

# 원본 파일의 내용 확인
with open('food.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))