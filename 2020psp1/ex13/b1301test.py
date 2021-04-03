from collections import namedtuple
Student=namedtuple('Student','name number sex')
taro=Student('Taro Chodai',12345678,'male')
hanako=Student('Hanako Nagasaki',12345679,'female')
print(taro.name)
print(taro.number)
print(taro.sex)
print(hanako.name)
print(hanako.number)
print(hanako.sex)

class Student:
    def __init__(self,name,number,sex):
        self.name=name
        self.number=number
        self.sex=sex

taro=Student('Taro Chodai',12345678,'male')
hanako=Student('Hanako Nagasaki',12345679,'female')
print(taro.name)
print(taro.number)
print(taro.sex)
print(hanako.name)
print(hanako.number)
print(hanako.sex)

class Joho_Student(Student):
    base_number=12345500
    def __init__(self,name,sex,shozoku_course):
        Joho_Student.base_number+=1
        super().__init__(name,Joho_Student.base_number,sex)
        self.shozoku_course=shozoku_course
    def aisatsu(self):
        print('Hello, I am '+self.name+'in '+self.shozoku_course+' course. My number is'+str(self.number)) #個人で処理が異なる場合はインスタンスメソッドで処理する。
    def aisatsu2():
        print('Hello, We are Joho Students!') #クラス全員に共通する処理はクラスメソッドという。

Jiro=Joho_Student('Jiro Joho','male','IS')
Saiko=Joho_Student('Saiko Deta','female','DS')
Joho_Student.aisatsu2()
Jiro.aisatsu()
Saiko.aisatsu()
