# 클래스

class Person :
    def __init__(self,name,age,addr):     #__init__ : 생성자
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAddr(self):
        return self.addr

    def toString(self):
        return self.name + "|"+self.age +"|"+self.addr

# list = [Person('홍길동','55','대구'),Person('이태수','66','울산'),Person('김상수','11','인천')]
# print(list)

hong = Person('홍길동','55','대구')
print(hong)
# print(hong.name, hong.age, hong.addr)
# print(hong.getName())
# print(hong.getAge())
# print(hong.getAddr())
# print(hong.toString())

# Class 변수( 자바 static 변수와 유사 )
class MyClass:
    num1 = 0 #클래스 변수( 모든 객체가 공유하는 num )

    def __init__(self, num2):
        self.num2 = num2 #self.num2 인스턴스 변수( 해당 객체에 저장되어 있는 num )

    def inc_class_var(cls):
        cls.num1 += 1

    def __str__(self):
        return "인스턴스 num2 : " + str(self.num2) + " 클래스 num1 : " + str(self.num1)

ob1 = MyClass(10)
# ob1.inc_class_var()
ob2 = MyClass(20)
# ob2.inc_class_var()
print(ob1)
print(ob2)
