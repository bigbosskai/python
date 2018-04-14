class Animal(object):
	def eat(self):
		print("-----eat-----")
	
class Dog(Animal):
	pass

Cat=type('Cat',(Animal,),{})

wangcai=Dog()
xiaohua=Cat()

wangcai.eat()
xiaohua.eat()