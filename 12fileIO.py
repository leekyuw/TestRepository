#파일 쓰기

#문법 open('파일 경로', '파일 모드')
#파일모드
# r : 읽기 모드
# w : 쓰기 모드
# a : 추가 모드
# x : 배타적생성모드 ( 파일이 이미 존재하는 경우 오류를 발생하는 모드 )


# 쓰기모드
# file = open("file1.txt",'w')
# file.write("HELLO WORLD my name is")
# file.close()

# 추가모드
# file = open("file1.txt",'a')
# file.write("TESTTEST TEST TEST\nTESTTEST TEST TEST\nTESTTEST TEST TEST\nTESTTEST TEST TEST\n")
# file.close()

#읽기 모드
# file = open("file1.txt",'r')
# str = file.readline()
# print(str)
# file.close()


# try:
#     file = open("file2.txt", "x")
#     file.write("TEST")
# except FileExistsError as e:
#     print(e)
# finally:
#     if file is not None:
#         file.close()

# with 예약어 - file.close() 자동 처리
# file = open("file1.txt",'w')
# file.write("MYNAME IS")
# flie.close()

try:
    with open("file1.txt", 'w') as file:
        file.write("MYNAME IS")
except FileExistsError as e:
    print(e)

# 콘솔창에서 처리하는 메모장 만들어봅니다.
# def menu() 메뉴함수
# 1. 파일 쓰기 - open, input ... 파일생성 -> 내용쓰기
# 2. 파일 수정 - 덮어쓰기
# 3. 파일 삭제 - 내용제거 ''
# 4. 종료      -  프로그램 종료
