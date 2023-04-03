# print(True)
# print(False)
# print(10==100)
# print(10!=100)
# x=25
# print(10<x<20)
# print("가방" == "가방")
# print("가방" == "오렌지")
# print("가방" >= "오렌지" )
# print("가방" <= "오렌지" )

#논리 연산자 and( && ), or( || ), not( ! )
# print(not True)
# print(not False)
# print(True and True)
# print(False and True)
# print(True and False)
# n1 = int(input("n1 > "))
# n2 = int(input("n2 > "))
# print(n1>n2 and n1 > 20)

# if:   종속에 주의해야된다.
# if False :
#     print("참입니다.-1")
# print("참입니다.-2")

#짝 홀수( %, 끝한자리, in )
# num = input("num > ")
# ln = int(num[1])
# print(ln)
# if ln==2 or ln==4 or ln==6 or ln==8 or ln==10 :
#     print('짝수입니다.')
#
# if str(ln) in "2468" :
#     print("짝수입니다.")
#
# if ln % 2 == 0:
#     print("짝수입니다.")


#양 음수
# num = int(input("num > "))
# if num > 0 :
#     print('양수입니다.')
# else:
#     print('음수입니다.')


# datetime 모듈 사용
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시간")
# print(now.minute,"분")
# print(now.second,"초")

# # 오전 오후
# if now.hour < 12:
#     print('오전입니다.')
# elif now.hour < 18:
#     print('오후입니다.')
# else:
#     print('저녁입니다.')
# #계절 구분
# if 3<=now.month<=5:
#     print('{}달은 봄입니다.'.format(now.month))
# elif 6<=now.month<=8:
#     print('{}월은 여름입니다.'.format(now.month))

# #주의 : if문을 건너뛰고 해야될 경우
# if True:
#     pass
# else:
#     print("TEST")

a = int(input('국어 성적 > '))
b = int(input('수학 성적 > '))
c = int(input('영어 성적 > '))
total = (a + b + c) / 3
if total >= 90:
    print('A')
elif 80 <= total <= 89:
    print('B')
elif 70 <= total >= 79:
    print('C')
elif 60 <= total >= 69:
    print('D')
elif total < 60:
    print('F')