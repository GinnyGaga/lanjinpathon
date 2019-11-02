# 类的构造方法
class Person():
    name = "小明"
    sex = "男"
     
    #构造方法,固定写法，初始化类
    def __init__(self,xb,mz):
        self.sex = xb
        self.name = mz
        self.test()

    def test(self):
        print("这是test方法")
    
d = Person("女","小王")
print(d.sex)
print(d.name)     