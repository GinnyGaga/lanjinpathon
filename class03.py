# 类的继承

#类与类之间的关系，继承
#重写
class Animal():
    weight = 90
    def run(self):
        print("动物能跑")

class Human(Animal):
    pass
    weight = 100 #重写


A = Human() #实例化人类，但是人类继承了动物类的属性和方法
print(A.weight) #子类调用父类的属性
A.run() #子类调用父类的方法
