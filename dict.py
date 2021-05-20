#coding=utf-8

dic = {'k1':'v1','k2':'v2'}

# 通过key获取value的方式：
# 1: 通过下标
# 2: get()
getkey = dic['k1'] 
print(getkey)
getkey = dic.get('k1','默认值')
print(getkey)

# 遍历字典
# 遍历key值
print('方式1')
for key in dic.keys():
    print(key,dic[key])

# 遍历value值
for value in dic.values():
    print(value)

# 遍历字典项
for kv in dic.items():
    print(kv)

# 遍历字典健值
for key,value in dic.items():
    print(key,value)


# 取出k1,并从字典中删除k1
dic.pop('k1')

# 清空字典
dic.clear()