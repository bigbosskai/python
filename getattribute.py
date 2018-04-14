class A(object):
	def __init__(self,subject1):
		self.subject1=subject1
		self.subject2='cpp'
	def __getattribute__(self,obj): #obj--->"subject1"
		if obj=='subject1':
			print('log subject1')
			return None
			return 'redirect python'
		else:#-----delete 2 rows lead to can not find subject2
			return object.__getattribute__(self,obj)
	def show(self):
		print('this is show funcion')

s=A("python")
print(s.subject1)
print(s.subject2)
s.show()