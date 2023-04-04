#딕셔너리 기본
dic_a = {
    "name" : "홍길동",
    "age" : "55",
    "job" : "프로그래머",
    "hobby" : ['등산', '수영', '독서'],
    "certification" : ['정보처리기사', '컴퓨터활용능력','SQLD']
}

# print(dic_a)
# print(dic_a['name'])
# print(dic_a['age'])
# print(dic_a['job'])
# print(dic_a['hobby'])
# print(dic_a['certification'][0])
#
# dic_a['add'] = "대구광역시 달서구"
# print(dic_a)
# del dic_a['job']
# print(dic_a)
# print(dic_a.keys())
# print(dic_a.get('name'))
# for key in dic_a:
    # print(key, " : ",dic_a[key])
    # print(key)

#깊은 복사 & 얕은 복사
# list_a = [10, 20, 30]
# list_b = list_a # 얕은 복사( 주소 복사 )
# list_c = list_a.copy() # 깊은 복사 ( 공간 따로 생성 + 값 복사 )
# list_a[1] = 100
#
# print("list_a :",list_a)
# print("list_b :",list_b)
# print("list_c :",list_c)

students = {
    'Tom' : 90,
    'Jane' : 85,
    'Mike' : 95,
    'John' : 80,
    'Anna' : 92
}
total = sum(students.values())
print(total)
num = 0
avg = 0
for key in students:
    num += students[key]
    avg = num/ len(students)
print(avg)
