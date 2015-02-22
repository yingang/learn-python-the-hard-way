#coding=utf-8

class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)


hall = Room("Hall",
"""
\n大厅里有个外星人在前面，挡住了去军火库的路，怎么办？[shoot|dodge|joke]
""")

armory = Room("Armory",
"""
嘿，我给你讲个笑话吧，真地很好笑诶，哈哈哈哈
乘着外星人笑得花枝乱颤的时候。。。我赶紧闪！
\n来到军火库了，不妙，柜子要用密码打开，请输入三位数字密码。
友情提示，连续输入错误三次，就再也打不开了哈！
""")

bridge = Room("Bridge",
"""
我靠，这都能猜中，看源码了吧
\n从军火库拿了炸弹之后，赶紧去往逃生舱
不料路上又杀出来几个外星人，怎么办？[throw|place]
""")

escape_pod = Room("EscapePod",
"""
我一边用枪指着炸弹，一边走向逃生舱，然后将炸弹放在门口外
乘外星人发愣之时，嗖地一下跳出门外并随即关上门，阿门，亲爱的逃生舱我来啦！
\n舱室内有五个逃生筏，我靠看上去没几个是好的，是死是活看运气了，挑一个吧
""")

winner = Room("Winner",
"""
走狗屎运啦，拜拜，各位可爱的外星人亲！
\nYOU WIN!
""")

loser = Room("Loser",
"""
我靠。。。
\nGAME OVER!
""")

generic_death = Room("Death", "You died")

shoot_death = Room("Death", "我打，我打。。。没打到，要死了。。。")

dodge_death = Room("Death", "我闪，我闪。。。哎呀，摔了一跤，要死了。。。")

guess_death = Room("Death", "哎，明明不知道还要死猜，你当是拍电影啊")

throw_death = Room("Death", "慌乱之中炸弹爆炸，大家一起去觐见宇宙大帝。。。")

escape_pod.add_paths({
	'2': winner,
	'*': loser})
	
bridge.add_paths({
	'throw': throw_death,
	'place': escape_pod})
	
armory.add_paths({
	'132': bridge,
	'*': guess_death})
	
hall.add_paths({
	'shoot': shoot_death,
	'dodge': dodge_death,
	'joke': armory})

START = hall