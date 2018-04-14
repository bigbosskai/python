from multiprocessing import Process
import time

def test():
	while True:
		print("--test--")
		time.sleep(1)

p=Process(target=test)
p.start()
#主进程挂了然后控制不退出

#等着所有的子进程结束我这个父亲在结束