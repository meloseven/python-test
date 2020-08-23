#lambba
sum = lambda a,b:a+b
print(sum(1, 2))

#列表推导式
vec = [1,2,3]
print([ x*2 for x in vec])
print([ [x, x*2] for x in vec])
print([ x*2 for x in vec if x > 1])

vec1 = [2, 4, 6]
vec2 = [1, 3, 5]
print([ x+y for x in vec1 for y in vec2])
print([ vec1[x]-vec2[x] for x in range(len(vec1)) ])

#字典推导
print({ x: x*2 for x in (2, 4, 6)})