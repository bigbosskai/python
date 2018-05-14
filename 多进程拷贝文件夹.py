from multiprocessing import Queue,Pool,Manager
from multiprocessing import Pool
import os
def copytask(name,oldfolername,newfolername,q):
	"""
		完成拷贝文件的功能
	"""
	fr=open(oldfolername+"/"+name,"r")
	fw=open(newfolername+name,"w")
	
	fw.write(fr.read())
	
	fr.close()
	fw.close()

	q.put(name)


def main():
	#获取用户copy文件夹的名字
	oldfolername=input("文件夹：")
	newfolername=oldfolername+"-复件"

	#获取old文件夹中所有的文件
	filenames=os.listdir(oldfolername)

	#创建一个文件夹
	os.mkdir(newfolername)



	po=Pool(3)
	q=Manager().Queue()
	for name in filenames:
		po.apply_async(copytask,(name,oldfolername,newfolername,q))

	num=0
	allnum=len(filenames)
	while num<allnum:
		q.get()
		num=num+1
		print("\r%.2f%%"%(num/allnum*100))
	print("copy end")
	#这里不用谢po.close() po.join()


if __name__=="__main__":
	main()


