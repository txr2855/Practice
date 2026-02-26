# 3，字符串常见操作
# 3.1 find
# find：检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就返回-1
# find(子字符串，开始位置下标，结束位置下标)
# 开始位置和结束位置下标可以省略，就表示在整个字符串中查找
# name = "mingming"
# print(name.find("i"))  # 第一个i的下标为1
# print(name.find("ming"))  # 0 检测到第一个ming的第一个下标为0
# print(name.find("m", 3))  # 返回的就是4，因为从3开始的
# print(name.find("m",5))  # 返回-1，超出范围，不包含返回-1
# print(name.find("m", 3,5))  # 在下标3-5的范围查找
# # 这些同样包前不包后
# print(name.find("m", 3,4))  # 仍然返回-1，因为他不查找4


# 3.2 index():检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否则就报错
# index(子字符串,开始位置下标,结束位置下标)
# 开始位置和结束位置下标可以省略，就表示在整个字符串中查找
# name = "我命由我不由天"
# print(name.index("命"))     # 1
# # print(name.index("命",2))  # 会报错，因为下标2往后找不到
# print(name.index("命",1,3))  # 1
# # 同样遵循包前不包后的原则
# # 这俩一个返回-1，一个报错
# find()：容错性高，找不到子串返回 -1，程序不会中断；
# index()：严格校验，找不到子串直接抛出 ValueError 异常，程序中断。
# 实际开发中，若不确定子串是否存在，优先用 find()（避免程序报错）；若确定子串一定存在，可用 index()（更直观）。


# 3.3 count() : 返回某个子字符串在整个字符串中出现的次数,没有就返回零
# count(子字符串，开始位置下标，结束位置下标)
# name = "mingming"
# print(name.count("m"))  # 2
# print(name.count("a"))  # 0
# print(name.count("m", 1))  # 1个，因为第一个m在0处
# print(name.count("m", 1, 3))  # 0
# # 也是包前不包后
# print(name.count("m", 2, 4))  # 0
# print(name.count("m", 2, 5))  # 1


# 3.4 判断
# 1,startswith()，是否以某个字符串开头，是的话就返回True，不是就False，如果设置开始和结束下标则在指定范围内查找
# startswith(子字符串，开始位置下标，结束位置下标)
# st = "sixstar"
# print(st.startswith("s"))  # True
# print(st.startswith("six"))  # True
# print(st.startswith("sex"))  # False
# print(st.startswith("s", 0, 1))  # True
# print(st.startswith("s", 3, 6))  # True
# print(st.startswith("s", 2, 6))  # False
# print(st.startswith("s", 2, 100))  # False


# 2.endswith()是否以某个字符串结尾，是的话就返回True，不是就False，如果设置开始和结束下标则在指定范围内查找
# endswith(子字符串，开始位置下标，结束位置下标)
# st = "sixstar"
# print(st.endswith("r"))   # True
# print(st.endswith("er"))  # False

# 3 isupper() 检测所有的字母是否都为大写，是就返回True
# st = "sixstar"
# print(st.isupper())  # False
# print("STR".islower())   # False
# print("str".islower())  # True

# 3.5 修改元素
# 1.replace():替换
# name = "好好学习天天向上"
# # 语法：replace(旧内容，新内容，替换次数)
# # 注意：替换次数可以省略，默认全部替换
# print(name.replace("天", "时"))
# print(name.replace("天", "时",1))


# 2 分割 split():指定分割符来切字符串
# st = "hello , world"
# print(st.split(","))  # 以列表的形式返回，得['hello ', ' world']
# # 如果字符串中不包含分割内容就不进行分割，会作为一个整体
# print(st.split("a"))  # 得['hello , world']
# print(st.split("o"))  # 得['hell', ' , w', 'rld']
# print(st.split("o",1))  # 指定只分割一次


# 3.capitalize() 作用：第一个字符大写
# st = "mingming"
# print(st.capitalize())  # Mingming

# 4.lower() 作用：大写转小写
# st = "NHWOS"
# print(st.lower())  # nhwos

# # 5.upper()  小写转大写
# st = "mdeonmqaod"
# print(st.upper())  #MDEONMQAOD
"""
AI总结：
# Python 字符串常见操作 核心总结
=========================================
一、查找类操作（找位置/存在性）
-----------------------------------------
1. find()
   - 功能：检测子串是否存在，存在返回起始下标，不存在返回 -1
   - 语法：str.find(子串, 开始下标, 结束下标)
   - 规则：包前不包后，省略范围则查找整个字符串
   - 示例："mingming".find("m", 3) → 4

2. rfind()
   - 功能：反向查找子串，存在返回起始下标，不存在返回 -1
   - 语法：str.rfind(子串, 开始下标, 结束下标)
   - 规则：从右往左找，下标仍为正向；包前不包后

3. index()
   - 功能：检测子串是否存在，存在返回起始下标，不存在抛出 ValueError 异常
   - 语法：str.index(子串, 开始下标, 结束下标)
   - 规则：包前不包后，省略范围则查找整个字符串

【核心区别】find() 返回 -1（不报错），index() 直接报错 → 不确定子串存在时优先用 find()

=========================================
二、统计类操作
-----------------------------------------
1. count()
   - 功能：统计子串出现次数，不存在返回 0
   - 语法：str.count(子串, 开始下标, 结束下标)
   - 规则：包前不包后，省略范围则统计整个字符串
   - 示例："mingming".count("m", 2, 5) → 1

=========================================
三、判断类操作（返回布尔值 True/False）
-----------------------------------------
1. startswith()
   - 功能：判断是否以指定子串开头
   - 语法：str.startswith(子串, 开始下标, 结束下标)
   - 规则：包前不包后，省略范围则判断整个字符串

2. endswith()
   - 功能：判断是否以指定子串结尾
   - 语法：str.endswith(子串, 开始下标, 结束下标)
   - 规则：包前不包后，省略范围则判断整个字符串

3. isupper()
   - 功能：检测所有字母是否为大写（非字母不影响）
   - 示例："STR".isupper() → True，"Str".isupper() → False

4. islower()
   - 功能：检测所有字母是否为小写（非字母不影响）
   - 示例："str".islower() → True，"STR".islower() → False

=========================================
四、修改/转换类操作（字符串不可变，返回新字符串）
-----------------------------------------
1. replace()
   - 功能：替换子串
   - 语法：str.replace(旧子串, 新子串, 替换次数)
   - 规则：省略次数则全部替换
   - 示例："好好学习天天向上".replace("天", "时", 1) → "好好学习天时向上"

2. split()
   - 功能：按指定分隔符分割字符串，返回列表
   - 语法：str.split(分隔符, 分割次数)
   - 规则：无分隔符则返回 [原字符串]；省略次数则全部分割
   - 示例："hello , world".split("o", 1) → ['hell', ' , world']

3. capitalize()
   - 功能：第一个字符大写，其余字符小写
   - 示例："mingming".capitalize() → "Mingming"

4. lower()
   - 功能：所有大写字母转小写（非字母不变）
   - 示例："NHWOS".lower() → "nhwos"

5. upper()
   - 功能：所有小写字母转大写（非字母不变）
   - 示例："mdeonmqaod".upper() → "MDEONMQAOD"

=========================================
# 通用核心规则
1. 范围参数均遵循「包前不包后」（包含开始下标，不包含结束下标）；
2. 字符串是不可变类型，修改类方法不会改变原字符串，需接收返回值；
3. 查找/统计类方法省略范围参数时，默认操作整个字符串。
"""
# 4 列表
# 基本格式：
# 列表名 = [元素1，元素2，元素3..]
# 注意：
# 所有元素放在[]内，元素与元素之间用逗号隔开
# 元素之间的数据类型可以各不相同


# 5.列表的常见操作
# 5.1添加元素
# append()  extend() 和insert()
# li = ["one", "two", "three"]
# # # li.append("four")  # ['one', 'two', 'three', 'four']
# # print(li)
# li.extend("four")  # ['one', 'two', 'three', 'f', 'o', 'u', 'r']
# print(li)
# # append整体添加,extend分散添加,将另一个列表的元素逐一添加
# li.insert(3, "four")
# # 在指定位置插入元素,如果有原有的元素,原来的元素会往后移动
# # li.insert("four") #报错,必须有下标
# print(li)
# li = [1, 2, 3]
# # li.extend(4)  #会报错,extend里面必须是可迭代对象啊啊
# # li.append(4)
# print(li)
# li.insert(3, 4)
# print(li)

#  5.2 修改元素,之间通过下标就可以修改
# li = [1, 2, 3]
# print(li[1])
# li[1] = "a"
# print(li)
# # 直接通过下标就能修改了

# 5.3 查找元素
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(1 in li)
# print(1 not in li)
# in:判断指定元素是否在列表中,如果在就返回True,不在就False
# not in:判断指定元素是否在列表中,如果在就返回False,不在就True
# li = ["a", "b", "c"]
# print("a" in li)  # True
# print("b" not in li)  # False
# 都一样啊

# 用户名称不能重复的案例
name_list = ["joker"]
while True:
    name = input("请输入你的名字,如果添加结束请按d退出")
    if name == "d":
        break
    print(name)
    # name in name_list  #这一行是多余的啊
    if name in name_list:
        print("已经被占用了")
    else:
        print(f"ok,你的名字是{name}")
        name_list.append(name)
        print(name_list)
# # 自己乱写的案例
# 其实还有index:返回指定数据的下标,如果查找不存在就报错
# count:统计指定数据在当前列表=出现的次数
# 跟字符串中的用法相同
"""
今日收获
字符串操作：掌握了查找（find/index，核心区别是 find 返回 - 1、index 报错）、统计（count）、
判断（startswith/endswith/isupper/islower）、修改（replace/split/capitalize/lower/upper）四类操作，
所有范围参数均遵循「包前不包后」，且字符串不可变，修改操作返回新字符串。
列表操作：理解列表是有序可变容器，掌握添加（append 整体加 /extend 拆分加 /insert 指定位置加）、
修改（下标直接赋值）、查找（in/not in 判断存在性）核心操作，extend 需传入可迭代对象，否则报错。
实战应用：用列表 + 循环 + in 判断实现了用户名防重注册功能，能通过 break 控制循环退出，
理解了基础业务场景的代码落地逻辑。
"""
