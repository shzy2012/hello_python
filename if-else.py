#coding=utf-8

# 如果条件成立,w=1 否则w='ap'
w = 1 if True else 'ap'
print(w)

# 多个条件
pos = [1,'ap']
if w==1 or w=='ap' in w in pos:
    print('ok')