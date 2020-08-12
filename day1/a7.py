# 集合
sites = {'Google', 'Taobao', 'Facebook', 'Facebook'}

print(sites)

# 成员测试
if 'Taobao' in sites :
    print('Taobao 在集合中')
else :
    print('Taobao 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(b - a)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素
