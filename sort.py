'''
sort 与 sorted 函数

sort()函数与sorted()函数区别是:sort()对已存在的列表进行操作,sorted()是返回一个新的list,不在原来的list上进行操作
'''

a = [2, 1, 4, 9, 6]
a.sort()
print(a) # 排序
 
c = [2, 1, 4, 9, 6]
d = sorted(c)
print(d) # 排序
print(c) # 未排序

