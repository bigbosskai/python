import functools
def note(func):
	"note function"
	@functools.wraps(func)
	def wrapper():
		"wrapper function"
		print("note somethine")
		return func()
	return wrapper

@note
def test():
	"test function"
	print("i am test")

print(help(test))