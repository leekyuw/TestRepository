# # Set 생성
# set1 = {10, 20, 30, 40, 50, 50}
# set2 = {20, 70, 30, 40, 55, 90}
# # print(set1)
# #
# # for i in set1:
# #     print(i)
#
# # 교집합
# result1 = set1.intersection(set2)
# print(result1)
#
# # 합집합
# result2 = set1.union(set2)
# print(result2)
#
# # 차집합
# result3 = set1.difference(set2)
# print(result3)
#
# # 컬렉션 -> Set 변환 함수 set()
# list_a = [10, 20, 30, 40, 50]
# print(list_a)
# print(set(list_a)) # 중복 없애기
# print(list(set(list_a))) #set->list 변경
# print(sorted(list(set(list_a)))) #set -> list변경
# print(sorted(list(set(list_a)),reverse=True)) #set -> list변경
import random
import time
# # 1부터 45까지의 숫자 중에서 6개를 선택
# lotto_numbers = random.sample(range(1, 46), 7)
#
# # 선택된 로또 번호를 오름차순으로 정렬
# lotto_numbers.sort()
#
# # 생성된 로또 번호 출력
# print("로또 번호 : ", lotto_numbers)

lotto_set = {random.randint(1, 45)}
while True:
    if len(lotto_set) == 7:
        break
    lotto_set.add((random.randint(1,45)))
    # print(random.randint(1, 45))
    # time.sleep(0.5)
lotto_list = sorted(list(lotto_set))
print(lotto_list)









