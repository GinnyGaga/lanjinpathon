import pymysql
"""
1、连接数据库
2、选择数据库
3、获取游标 
4、增删改查

"""
#     # 数据库的查询方法 1
# db = pymysql.connect(host="localhost",user="root",password="123456",db="ginnydata") #连接数据库
# cursor = db.cursor() #获取游标
# cursor.execute("select * from tt_class") #执行语句
# res = cursor.fetchall() #获取查询结果
# db.close() # 关闭数据库
# print(res)

# # 数据库的查询方法 2
# for i in ["tt_class","tt_student","tt_grade"]:
#     db = pymysql.connect(host="localhost",user="root",password="123456",db="ginnydata") #连接数据库
#     cursor = db.cursor() #获取游标
#     cursor.execute("select * from {};".format(i)) #执行语句
#     res = cursor.fetchall() #获取查询结果
#     db.close() # 关闭数据库
#     print(res)


# # 数据库的查询方法 3
# def query(sql):  #定义方法：def 方法的名字（参娄1,参数2,...）
#     """
#     这是数据库的查询方法
#     """
#     db = pymysql.connect(host="localhost",user="root",password="123456",db="ginnydata") #连接数据库
#     cursor = db.cursor() #获取游标
#     cursor.execute(sql) #执行语句
#     res = cursor.fetchall() #获取查询结果
#     db.close() # 关闭数据库
#     print(res)

# query("select * from tt_grade;")
# query("show tables;")
# query("desc tt_class;")

# # 数据库的查询方法 4
# def query(sql):  #定义方法：def 方法的名字（参娄1,参数2,...）
#     """
#     这是数据库的查询方法
#     """
#     db = pymysql.connect(host="localhost",user="root",password="123456",db="ginnydata") #连接数据库
#     cursor = db.cursor() #获取游标
#     cursor.execute(sql) #执行语句
#     res = cursor.fetchall() #获取查询结果
#     db.close() # 关闭数据库
#     print("哈哈")
#     return res

# query("select * from tt_student;") #获取不到结果

# aa = query("show tables;")
# print(aa)  

# bb = query("select * from tt_grade")
# cc = []
# for i in bb:
#     cc.append(i[2])
#     print(i) #打印tt_grade表单

# # print(cc) #打印tt_grade表单里的语文成绩，语文成绩下标是2

# # 数据库的修改方法 
# def commit(sql):  #定义方法：def 方法的名字（参娄1,参数2,...）
#     """
#     这是数据库的修改方法
#     """
#     db = pymysql.connect(host="localhost",user="root",password="123456",db="ginnydata") #连接数据库
#     cursor = db.cursor() #获取游标
#     cursor.execute(sql) #执行语句
#     # db.commit() #提交修改及应用改变
#     res = cursor.fetchall() #获取查询结果
#     db.close() # 关闭数据库
#     print(res)

# # commit("insert into tt_class (id,cname) values (5,'小苹果');") # 每次运行都是提交一次，重复运行将会让主键重复，导致提交失败
# commit("select * from tt_class;")

# try...except...的用法
def query(sql):  
    """
    这是数据库的查询方法
    """
    db = pymysql.connect(host="localhost",user="root",password="123456",db="ginnydata") #连接数据库
    cursor = db.cursor() #获取游标
    try:
        cursor.execute(sql) #执行语句
        res = cursor.fetchall() #获取查询结果
        db.close() # 关闭数据库
        print(res)
        return True
    except:
        return "SQL语句错误，请检查后输入"

aa = query("select * from tt_student where id = 8;") 
print(aa)





# # 统计数组相同值的个数 方法1
# xx = [1,5,6,99,23,44,85,44,44,7]
# a = xx.count(44)
# print(a)

# # 统计数组相同值的个数 方法2
# xx = [1,5,6,99,23,44,85,44,44,7]
# x = 0
# for i in xx:
#     if i == 44:
#         x = x + 1
# print(x)

# # 统计数组相同值的个数 方法3
# def count(value):
#      xx = [1,5,6,99,23,44,85,44,44,7]
#      x = 0
#      for i in xx:
#         if i == value:
#             x = x + 1
#      print(x)

# count(6)

# # 统计数组相同值的个数 方法4
# def count(value):
#      xx = [1,5,6,99,23,44,85,44,44,7]
#      x = 0
#      for i in xx:
#         if i == value:
#             x = x + 1
#      print("返回的结果为：",x)
#      return x  #如果没有return,那么方法外部就取不到结果，只能返回None.

# aa = count(44)
# print(aa)