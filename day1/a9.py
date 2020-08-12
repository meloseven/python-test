# 类型转换
import math

print(chr(1000))
print([1,2] == [1,2])
print((20 , 'xxx', [1,2]) == (20 , 'xxx', [1,2]))
print({'a', 'b'} == {'a', 'b'})
print({'a': 1, 'b': 2} == {'a': 1, 'b': 2})

a = 10
b = 20
print(a and b)
print(a or b)
print()

a = []
print(a and b)
print(a or b)
print()

a = [2, 3]
print(a and b)
print(a or b)
print()

a = {}
print(a and b)
print(a or b)
print()

print(0.1 + 0.2)
print(7//2.22)
print(math.pi)