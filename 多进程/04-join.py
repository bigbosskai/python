from multiprocessing import Process
import time
import random

def test():
	for i in range(random.randint(1,5)):
		print("----%d---"%i)
		time.sleep(1)

p=Process(target=test)
p.start()
p.join()#test函数执行完毕后这个函数才解堵塞
#等待几秒

print("---main---")