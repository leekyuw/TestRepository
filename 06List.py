# #1 List기본
# list_a = [10,20,30,'c',"문자열",True,False]
# print(list_a)
#
# #2 요소에 접근
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[3])
# print(list_a[4])
# print(list_a[5])
# print(list_a[6])
#
# #3 요소값 변경
# list_a[0] = 'hong gil dong'
# print(list_a[0])
#
# #4 리스트 요소 이중접근
# print(list_a[4][1])

# list_b = [[10,20,30],[40,50,60],[70,80,90]]
# print(list_b)
# print(list_b[2])
# print(list_b[0][0])

# 반복문과 list
# for i in [0,1,2,3,4,5]:
#     print(i)
# list_a = [int(input('단수 입력 > ')),int(input('단수 입력 > ')),int(input('단수 입력 > '))]
# for i in list_a:
#     for j in range(1,10):
#         print(i,"x",j," = ", i*j)


# import tkinter as tk
# window = tk.Tk()
# window.title("Window Title")
# window.geometry("400x300")
# window.mainloop()

# 기존 list 값 추가
# list_c = [10,20,30]
# print(list_c)
# list_c.append(40)
# list_c.append('문자열')
# print(list_c)
# list_c.insert(0,123)
# print(list_c)
# list_c.extend([100,200,300])
# print(list_c)

# 7 요소 값 제거
# list_d = [10, 20, 30, 40, 50, 60, 70, 60, 70, 60, 70, 60, 70]
# print(list_d)
# del list_d[2] # index 요소 제거
# print(list_d)
# list_d.pop() # index 마지막 요소 제거
# print(list_d)
# del list_d[1:4] # 슬라이싱을 사용하여 범위 삭제
# print(list_d)
# list_d.remove(60)
# print(list_d)
# print(set(list_d)) #리스트 안의 중복값 제거

# 8 list 내부 값 탐색
# list_e = [10,20,30,40,50,60]
# print(15 in list_e)
# print(20 in list_e)
# print(15 not in list_e)
# print(20 not in list_e)
# # list 길이
# print(len(list_e))


# while True:
#     cnt = 0;
#     num = [int(input('num > '))]
#     if num[cnt] == -1:
#         for i in range(0,num.len-1):
#              += num[i]
#         break
#     cnt += 1

list = []
while True:
    data = int(input("입력[종료: -1] : "))
    if(data == -1):
        break
    list.append(data)
print(list)
# max=list[0]
# min=list[0]
# for i in range(0, len(list)):
#     # if (max < list[i]):
#     #     max = list[i]
#     # if (min > list[i]):
#     #     min = list[i]
print("최대 : ", max)
print("최소 : ", max)
print("최대 : ", max(list))
print("최소 : ", min(list))
print("총합 : ", sum(list))
print("평균 : ", sum(list) / len(list))
