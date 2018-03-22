def test(a,b,*args,**kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)

test(1,2,3,4)
test(1,2,3,4)


test(1,2,3,4,aa=123,bb='abd')
dit=dict()
dit['mame']='bosskai'
dit['age']=12

print(dit)
print(**dit)
