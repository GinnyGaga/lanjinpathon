# 类
#普通变量
# a = [1,2,3]
# b = 1
# c = True
# def ccc():
#     print(b)

# 类包含属性（特征）和方法（行为、能干啥）

class Person():

    # 成员变量：无论哪个地方都能用成员变量
    name = "小猫"
    high = 188
    sex = "男"
    age = 18

    #成员方法：以self参数为开头的方法
    def sing(self):
        print("大家好，我会唱歌")
        print("我会哈哈")

    def eat(self):
        print("我很能吃")
    # 成员方法的传参
    def tiao(self,wd,sha):  # wd = "广场舞"，sha = "还有……"
        print("我会跳{}和{}".format(wd,sha))

    # self 的用法
    # self:类本身的实例化，在类里边用。
    def rap(self):
        a = self.name #引用类的属性
        print(a)
        self.sing() #引用类的成员方法


#实例化类：P是Person类的实例化
#引用类，来是放在类里边，只能放在类外边
P = Person() # 赋值
# N = P.name # 引用类的成员变量
# print(N)  
# P.sing()  #引用类的成员方法
# P.tiao("广场舞","还有……") #成员方法的传参
P.rap() # self在类里边引用变量和方法


