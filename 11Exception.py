# n = input('정수입력 >')
# print(n+1)

#예외 기본
# try:
#     print(10/0)
# except:
#     print("예외 발생..")
#
# #예외 객체
# import traceback
#
# try:
#     print(10/0)
# except Exception as e:
#     print(e)
#     traceback.print_exc
#
# print("hello world")
# print("hello world")
# print("hello world")

#try - except - else
try :
    print("try영역 정상코드")
    # print("오류 발생!", 10/0)
except Exception as e:
    print('예외 처리',e)
else:
    print('else','예외가 발생하지 않을때 실행')
finally:
    print('finally','예외발생과 무관하게 무조건 실행')

print("hello world")
print("hello world")
print("hello world")

#try - except - finally
