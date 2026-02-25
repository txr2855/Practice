# 1.字符串编码：
# 本质上就是二进制与语言文字的一一对应关系
# 1.2 Unicode：所有的字符都是两个字节
# 好处：字符和数字之间转换的速度更快一点
# 坏处：占用空间大


# 1.3 UTF-8：精准对不同的长度字符用不同的长度表示
# 好处：节省空间
# 缺点：字符与数字的转换的速度较慢，每次都要计算字符需要用多少个字符来表示
# 先简单了解一下


# 1.4 字符串编码转换
# a = "hello"
# print(a, type(a))  # str 字符串以字符为单位进行处理
# a1 = a.encode()  # 编码
# print("编码后", a1)
# print(type(a1))  # bytes
# """
# 字符串 (str)：以 Unicode 字符为单位处理，是人类可读的文本。
# 字节 (bytes)：以字节为单位处理，是计算机可直接存储和传输的二进制数据。
# """
# a2 = a1.decode()  # 解码
# print(a2)  # 又回hello了
# print(type(a2))  # str
# # 对于bytes，只需要知道他和字符串类型相互转换
# st = "我就是要学习python"
# st1 = st.encode("utf-8")
# print(st1, type(st1))
# st2 = st1.decode("utf-8")
# print(st2, type(st2))


# 2 字符串的常见操作
# 2.1  + 字符串拼接
# print(10+10)  # 这是算数运算符的+
# print("10"+"10")  # 得1010，是字符串拼接的+
# name1 = "love"
# name2 = "you"
# print(name1+' '+name2)
# print(name1+name2, sep="")
# print(name1, name2)


# 2，2  *重复输出
# print("hello world\n"*3, end="")  # 如果要换行要在里面加\n,但是他最后还有个\n，所以可以手动去了
# # 需要输出多少次，*后面就写多少
# print("杀杀杀\n"*3, end="")
# print("杀杀杀\t"*3, end="")


# 2.2 成员运算符
# 作用：检查字符串中是否包含了某个子字符串（即某个字符或多个字符）
# in: 如果包含返回True,不包含返回False
# not in:如果不包含返回True,包含返回False
# name = "hello world"
# print("a" in name)  # False
# print("h" in name)  # True
# print("a" not in name)  # True
# print("h" not in name)  # False
# print("hello" in name)  # True
# print("helo" in name)  # False  整体去找的啊

# 2.3 下标
# python中下标从零开始
# 作用：通过下标能快速找到对应的数据
# 格式：字符串名[下标值]
# name = "wukong"
# # 从左往右数，下标从0开始
# print(name[0])  # w,下接
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# # print(name[6])  # 报错了，一共就6个，不要超出下标范围。
# # 从右往左，下标从-1开始
# print(name[-1])
# print(name[-2])
# print(name[-7])  # 继续报错，超出索引范围


# 2.4切片
# 含义：指对操作迭代对象截取其中一部分的操作
# 语法：[开始位置:结束位置:步长]
# 包前不包后：即从起始位置开始，到结束位置前一位结束
# st = "asdfghjkl"
# # 从左往右
# print(st[0:3])  # asd     0,1,2,那个3取不了，但是从0开始算成1，还是3位
# print(st[3:7])  # fghj
# print(st[3:])  # fghjkl 下标为3之后的全部截取到了,包含3
# print(st[:7])  # asdfghj  下标为7之前的全部 截取到了，但是不包含7，包前不包后
# # 从右往左
# print(st[-1:])  # l
# print(st[:-1])   # 包前不包后，l切不到
# print(st[-1:-5])  # 啥也没有，这些都和步长息息相关，不写步长默认是1
# # 步长：表示选取间隔，不写为1，
# 绝对值大小决定切取的间隔，正负号决定方向
# 正数表示从左往右取值，负数表示从右往左取值
st = "asdfghjkl"
# print(st[-1::1])  # l
# # 你看-1表示l，步长为1，正数，从l往右，所以是l
# print(st[-1:-5])
# print(st[-1:-5:-1])
# # 你这取值往左，步长往右，打架说是,步长改成-的就行
print(st[0:7])
print(st[0:7:2])  # adgj 2个一取，不取最后一个
print(st[0:7:3])  # afj  3个一取













