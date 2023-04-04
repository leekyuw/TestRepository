# num = input('입력하세요 : ')
# print('입력 값은 : ', num)

# 반복문
# range( 반복 횟수 )
# for i in range(5):
#     print(i)
# print()
# for i in range(5, 11):
#     print(i)
# print()
# for i in range(0,10, 2):
#     print(i)

#range() 역방향
# for i in range(5, -1, -1):
#     print(i)
# print()
# for i in reversed(range(5)):
#     print(i)

# num = int(input("num > "))
# for i in range(1,num+1):
#     if i % 3 == 0:
#         print("i : ", i)

# 구구단
# for dan in range(9, 1, -1):
#     print(dan,"단")
#     for i in range(9, 0, -1):
#         print(dan,"x",i,"=",dan*i)

# reverse 구구단
# for dan in reversed(range(2,10)):
#     print(dan,"단")
#     for i in reversed(range(1,10)):
#         print(dan,"x",i,"=",dan*i)

# h = int(input("h > "))
# for row in range(0,h):
#     for star in range(0, row+1):
#         print("*", end="")
#     print()

# h = int(input("h> "))
# for i in range(0,h):
#     # 공백
#     for j in range(0,(h-1)-i):
#         print(" ",end="")
#     # 별
#     for k in range(0, i*2+1):
#         print("*",end="")
#     print()

#  무한루프~

# import time
# # while True :
# #     print("*", end="")
# # print(time.time())
# num = time.time() + 5 # 5초후의 값이 num에 저장
# cnt = 0
# while True:
#     print("*",end="")
#     if(time.time() > num):
#         break
#     cnt += 1
# print("총 반복된 *개수는 {}개입니다.".format(cnt))

# continue
# for i in range(1,11):
#     if i % 3 == 0:
#         continue
#     print(i)