# List相关操作

list = [1, 2, '3', 4, 5]
print(list)
# 取值
print(list[0])
# 添加
list.append(6)
print(list)
# 插入
list.insert(0, -1)
print(list)
# 修改
list[1:2] = ['1', '2', '3']
print(list)
# 删除
list[1:5] = []
print(list)