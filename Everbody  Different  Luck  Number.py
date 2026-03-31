import random
while True:
	strl=input("请输入你的名字:")
	print("Hello! {}".format(strl))
	guard=ord(strl[0]) %  100
	print("你的幸运数字是",random.choice(range(guard)))
	choice=input("\n是否继续查询? (Y/N):")
	if choice.upper()!='Y':
		print("程序结束!")
		break
input("按ENTER退出...")
