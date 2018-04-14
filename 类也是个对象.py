class Person(object):
	num=0
	print('person')
	def __init__(self):
		pass

print(Person)



def chose_class(name):
	if name=='foo':
		class Foo(object):
			pass
		return Foo
	else:
		class Bar(object):
			pass
		return Bar


class Test1(object):
	pass

Test2=type("Test2",(),{})


t1=Test1()
t2=Test2()
print(type(t1))
print(type(t2))