class Test(object):
	def __call__(self):
		print("i am call function!")

t=Test()
t()


class Test2(object):
	def __init__(self,func):
		print("init over")
		print("i am init function")
		self.__func=func
	def __call__(self):
		print("i am call function")
		self.__func()


@Test2
def test():
	print("i am test")

test()
print(type(test))