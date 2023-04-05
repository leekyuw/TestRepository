# 함수 기본
# def print_3_times() :
#     print('안녕하세요')
#     print('안녕하세요')
#     print('안녕하세요')
#
# print_3_times()


# 매개변수
# def print_n_times(value, n):
#     for i in range(n):
#         print(value)
#
# print_n_times("Hello",5)


# 가변 매개변수
# def print_n_times(*value):
#     print(value) # 튜플형태로 가변인자를 받는다.
#     for i in value:
#         print(i)
#
# print_n_times("Hello","my","name","is","hong")


# 매개변수 디폴트 값
# def print_n_times(value, n=10):
#     for i in range(n):
#         print(value)
#
# print_n_times("Hello")


# 키워드 매개변수
# def print_n_times(*value, n):
#     for i in range(n):
#         for data in value:
#             print(value, end="")
#         print()
#
# print_n_times("Hello","my","name","is","hong",n=5)


# def test(a, b, c):
#     print(a + b + c)

# test(10,20,30)
# test(b=30,a=40,c=100)


# 리턴값 확인
# def test():
#     return 100
# print(test())

# 팩토리얼
# def factorial(n):
#     output = 1
#     for i in range(1, n+1):
#         output *= i
#     return output
#
# print("3!", factorial(3))

# def factorial2(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial2(n-1)
#
# print("3!", factorial2(4))


# 함수를 인자로 받는 함수
# def call_10_times(func):
#     for i in range(10):
#         func()
#
# def print_hello():
#     print('HELLO WORLD')
#
# call_10_times(print_hello())


# map() 함수 사용
# def power(item):
#     return item * item

# def under_3(item):
#     return item < 3

# 변수를 선언합니다.(리스트로 전달)
# list_input_a = [1, 2, 3, 4, 5]
# # map() 함수를 사용
# output_a = map(power, list_input_a)
# print(output_a)
# print(list(output_a))
# output_b = filter(under_3, list_input_a)
# print(output_b)
# print(list(output_b))



# def multiply_by_2(item):
#     return item*item
# print(list(map(multiply_by_2,[1,2,3,4,5])))
# def even_numbers(item):
#     return item % 2 == 0
# print(list(filter(even_numbers,[1,2,3,4,5])))


# # 람다
# # 함수 선언
# power = lambda item : item * item
# # power = lambda 매개변수 : 로직
# print(power(4))
#
# under_3 = lambda item : item < 3
# print(under_3(4))
#
# # 변수를 선언합니다.(리스트로 전달)
# list_input_a = [1, 2, 3, 4, 5]
# # map() 함수를 사용
# output_a = map(power, list_input_a)
# print(output_a)
# print(list(output_a))
# output_b = filter(under_3, list_input_a)
# print(output_b)
# print(list(output_b))
#
# output_c = map(lambda item : item * item, list_input_a)
# print(output_c)
# print(list(output_c))

numbers = [1,2,3,4,5]
result = [(lambda x: x* 2) (x) for x in numbers]
print(result)

def test(x) :
    return x*2
result2 = [test(x) for x in numbers]
print(result2)


