#coding=gbk

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
\n大厅里有个外星人在前面，挡住了去军火库的路，怎么办？[shoot|dodge|joke|exit]
""")

armory = Room("Armory",
"""
\n来到军火库了，不妙，柜子要用密码打开，请输入三位数字密码。
友情提示，连续输入错误三次，就再也打不开了哈！
""")

bridge = Room("Bridge",
"""
\n从军火库拿了炸弹之后，赶紧去往逃生舱
不料路上又杀出来几个外星人，怎么办？[throw|place]
""")

escape_pod = Room("EscapePod",
"""
\n舱室内有五个逃生筏，我靠看上去没几个是好的，是死是活看运气了，挑一个吧
""")

winner = Room("Winner",
"""
YOU WIN!
""")

loser = Room("Loser",
"""
GAME OVER!
""")

escape_pod.add_paths({
	'2': winner,
	'*': loser})
	
bridge.add_paths({
	'throw': loser,
	'place': escape_pod})
	
armory.add_paths({
	'0132': bridge,
	'*': loser})
	
hall.add_paths({
	'shoot': loser,
	'dodge': loser,
	'joke': armory})

START = hall