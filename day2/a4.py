def myFunc( name, age = 20, *other):
	print(name)
	print(age)
	print(other)

myFunc('melo', 30, 5, 6, [1,2])

def myFunc1(name, **other):
	print(name)
	print(other)

myFunc1('melo', age = 28, title = 'engineer')