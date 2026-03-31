hobbies = ''
for i in range(4):
	s=input('旅游、听歌、学习、游戏:')
	if s.upper() == 'Q':
		break
	hobbies += s+''
print('我为数不多的小爱好是:',hobbies)
