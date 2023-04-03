 #fomat()
# str = "TEST {}".format(10)
# print(str)
# print(type(str))
#
# str = "TEST {}".format('안녕하세요')
# print(str)
# print(type(str))

# 다중 서식문자 입력
# charge = 5000
# print("{}만 원".format(charge))
# print("파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000))
# print("{} {} {}".format(3000, 4000, 5000))
# print("{2} {1} {0}".format(1, "문자열", True))

#format() IndexError 예외
# format_a = "{} {}".format(1,2,3,4,5)
# format_b = "{} {} {]".format(1,2)
# print(format_b)

# apple = int(1000)
# totalApple = int(5)
# format_a = "사과 1개당 가격은 {} 원이고, 총사과판매액수는{}입니다.".format(apple,apple*totalApple);
# print(format_a)

#문자열 함수 종류
str = "hello world"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print("Hello ".strip())

print(str.startswith("he"))
print("w" in str)