import re

def showinfo():
	print('-'*30)
	print("学生管理系统v1.0")
	print("1.增加学生")
	print("2.删除学生")
	print("3.修改学生")
	print("4.查询学生")
	print("5.遍历学生")
	print("6.退出")
	print('-'*30)



students=[]


while True:
	showinfo()

	key=int(input("请根据序号选择功能："))

	if key==1:
		print("选择了新增")
		stuname=input("姓名：")
		stuid=int(input("id:"))
		stuage=int(input("age:"))

		

		leap=0

		for temp in students:
			if temp['id']==stuid:
				leap=1
				break

		if leap==0:
			stuinfo={}
			stuinfo['name']=stuname
			stuinfo['id']=stuid
			stuinfo['age']=stuage
			students.append(stuinfo)
			print("添加成功")
		else:
			print("已有该id,添加失败")
			break

	elif key==2:
		print("选择了删除")
		delid=int(input("需删除的Id:"))
		i=0
		leap=0
		for temp in students:
			if temp['id']==delid:
				leap=1
				break
			else:
				i=i+1

		if leap==1:
			del students[i]
			print("删除成功")
		else:
			print("无该学生，删除失败")

	elif key==3:
		print("选择了修改")
		choseId=int(input("需修改的id:"))
		i=0
		leap=0
		leap1=0
		for temp in students:
			if temp['id']==choseId:
				leap=1
				break
			else:
				i=i+1
		if leap==1:
			newinfo={}
			newstuname=input("姓名：")
			newstuid=int(input("id:"))
			for temp1 in students:
				if temp1['id']==newstuid:
					leap1=1
					break
			if leap1==1:
				print("该id已有,修改失败")
			else:		
				newstuage=int(input("age:"))
				newinfo['name']=newstuname
				newinfo['id']=newstuid
				newinfo['age']=newstuage
				students[i]=newinfo
				print("修改成功")

	elif key==4:
		print("选择了查询学生")
		findid=int(input("需查询的学生Id:"))
		i=0
		leap=0
		for temp in students:
			if temp['id']==findid:
				leap=1
				break
			else:
				i=i+1
		if leap==1:
			print("姓名:%s\nID:%d\nage:%d\n" % (temp['name'],temp['id'],temp['age']))
		else:
			print("没找到该学生")

	elif key==5:
		print("遍历学生")
		print('*'*20) 
		print("姓名    id    age")
		for temp in students:
			print("%s    %d    %d" % (temp['name'],temp['id'],temp['age']))
		print('*'*20) 

	elif key==6:
		question=input("确认退出吗？？？ yes or no:")

		if re.match(r'^[Yy]+(es|Es|ES|eS)?$',question):
			print("拜拜~")
			break
	else:
		print("选择有误")










