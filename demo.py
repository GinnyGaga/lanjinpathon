# print(123)
# print(12.33455)
# print("你好")
# print("你好",12345)


# a = int(input("第一个数字a:"))
# b = int(input("第二个数字b:"))
# c = a + b
# print(c)
# print("a > b 么？", a > b)
"""
x = len("123")
print(x)

y = len("abc")
print(y)

z = len("你好啊")
print(z)

"""
# 元组
# 数组
# yy = ["aa","fff","ddf","ccc"]
# yy.sort()
# print(yy)

# yy.append("ss")
# print(yy)

# yy.insert(1,"你好")
# print(yy)

# xx = yy.pop(1)
# print(xx)
# print(yy)
# xx = [1,2,3,1,1]
# xx = yy.copy()
# # print(xx)
# xx.clear()
# print(xx)
# t = xx.count(1)
# print(t)

#字典
# A = {"a":1,"b":2,"c":3}
# print(A)
#get
# B = A.get("c")
# print(B)
#pop
# C = A.pop("b")
# print(C)
# # #clear
# A.clear()
# print(A)
#copy
# D = {0:"AA",1:"BB"}
# print(D)
# D = A.copy()
# print(D)

# a = input("请输入:")
# aa = "{b}{b}{b}".format(b = a)
# print(aa)

# A = int(input("请输入你的成绩:"))
# if A == 100:
#     print("满分!")
# elif A < 60:
#     print("不及格!")
# elif 60 < A < 100:
#     print("及格啦!")
# else:
#     print("请重新输入")

# 1、九九乘法表

# i = 1
# for i in "123456789":
#     i = int(i)
#     if i <= 9:
#         j = 1
#         for j in "123456789":
#             j = int(j)
#             if j <= i:
#                 re = i * j
#                 print("{} * {} = {}".format(i,j,re))
             
    
#2、
# a = []
# b = []
# c = [34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
# for i in c:
#     if i > 100:
#         a.append(i)
#     else:
#         b.append(i)
# print("大于100的数组：",a)
# print("小于100的数组：",b)

# 3、
# N = int(input("请输入年："))
# Y = int(input("请输入月："))
# R = int(input("请输入日："))
# #闰年
# if N / 400 == 0:
#     t == 366

# #平年
# if N /400 > 0:
#     t = 365
# d = t - 33 * (12/Y) - R
# print("这是{}年的第{}天".format(N,d))
#5
# n = input("请输入：")
# m = n.index(0)
# print(m)
# n = int(n)
# print(n)