def parameter(str="string"):
	print(str)
	def de(func):
		def wrapper():
			print("---log1---")
			xx=func()
			print("---log2---")
			return xx
		return wrapper
	return de
@parameter("helloworld")
def test():
	print("i am test!")

test()