#coding=utf-8

'''
sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
'''

'''
sorted 语法
sorted(iterable, key=None, reverse=False)  
参数说明：
iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
'''

a = [2, 1, 4, 9, 6]
a.sort()
print(a) # 排序
 
c = [2, 1, 4, 9, 6]
d = sorted(c)
print(d) # 排序
print(c) # 未排序

print('\n')
# sorted() 函数可以接收任何的 iterable
s = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'},reverse=False)
print(s)

print('\n')

# 通过 key 的值来进行数组/字典的排序
array = [{"age":20,"name":"a"},{"age":30,"name":"b"},{"age":10,"name":"c"}]
array = sorted(array,key=lambda x:x['age'],reverse=True)
print(array)


#多列排序
print('先按照成绩降序排序，相同成绩的按照名字升序排序')
d1 = [{'name':'alice', 'score':38}, {'name':'bob', 'score':18}, {'name':'darl', 'score':28}, {'name':'christ', 'score':28}]
l = sorted(d1, key=lambda x:(-x['score'], x['name']))
print(l)