# 1 if判断
# age = 21
# if age < 18:
#     print("未成年不能上网")
# grade = input("你的成绩是？")  # 注意,input里面是字符串类型啊
# if grade == "100":
#     print("nb")
# if grade == "60":
#     print("ok")
# 现在就是先用字符串啊,之后再学后面的


# 运算符
# 2 比较(关系)运算符
# ==比较两个值是否相等,相等就返回为真True,不相等返回为假False.
# !=比较两个值是否相等,相等就返回为假False,不相等返回为真True.
# a = 666
# b = 999
# # print(a == b)  # False
# # print(a != b)  # Ture
# # print(a > b)  # False
# # print(a < b)  # Ture
# if a < b:
#     print('a < b')
# if a > b:
#     print('a > b')
#  3 逻辑运算符 与,或,非
# and(与)左右两边都符合为真
# a = "呵呵"
# b = "哈哈"
# if a == "呵呵" and b == "哈哈":
#     print("a和b都在傻乐")  # 能输出
# if a == "呵呵" and b == "嘿嘿":
#     print("a和b都在傻乐")  # 不能输出,嘻嘻不对
# or(或)左右两边只要有一个符合就为真,都对也为真,而且python左边真就不看右边了
# fruit = "苹果"
# if fruit == "苹果" or fruit == "香蕉":
#     print("我爱吃")
# # not(非)表示相反的结果
# print(3 > 9)
# # 输出False
# print(not 3 > 9)
# # 输出为True
# 友好提示用户输入成绩
# 4.三目运算(三元表达式)
# 基本格式:为真结果 if 判断条件 else 为假结果
# 5.if-else
# if条件:
#        满足条件干的事情
# else:
#    不满足条件干的事情
# a = 666
# if a == 999:
#     print("nb")
# else:      # else后面不能加其他条件
#     print("不nb")
# 如果不满足就是else输出,都要输出
# 三目运算(三元表达式)
# 基本格式:为真结果 if 判断条件 else 为假结果
# a = 5
# b = 8
# if a <= b:
#     print("a小于等于b")  # 为真结果
# else:
#     print("b比a大")  # 为假结果
# print("a小于等于b") if a <= b else print("b比a大")
# 其实主要用于赋值
# a = 160
# b = 160
# num = a if a > b else b
# print("最大的是%s" % num)
# if-else 二选一,if-elif结构,多选1
# if 条件1:
#     满足条件1做的事情1
# elif 条件2:
#     满足条件2做的事情2
# elif 条件3:
#     满足条件3做的事情
# 可以继续写,前面的符合就不看后面了
# score = 60
# if 85 <= score <= 100:
#     print("优秀")
# elif 70 <= score <= 85:
#     print("良好")
# elif 0 <= score <= 70:
#     print("不合格")
# else:
#     print("无效的")
#      如果用input需要改成整型啥的
# if 嵌套 if里面有if
# 注意,内外层的if判断,都可以是if-else
# 格式:
# if 条件1:
#     事情1
#     if 条件2:
#         事情2
# else:
#     不满足条件做的事情
# 假设要去买票量体温
# 设计一个bool型变量,代表有无车票
# 设计一个float型变量,代表体温
ticket = False
tem = 38
# if ticket == True:这两个是一个意思,默认的就是
if ticket:
    print("欢迎", end=" ")
    if tem >= 37.2:
        print("你发烧了")
    else:
        print("你没发烧")
else:
    print("你没有啊")
