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
\n�������и���������ǰ�棬��ס��ȥ������·����ô�죿[shoot|dodge|joke|exit]
""")

armory = Room("Armory",
"""
\n����������ˣ��������Ҫ������򿪣���������λ�������롣
������ʾ����������������Σ�����Ҳ�򲻿��˹���
""")

bridge = Room("Bridge",
"""
\n�Ӿ��������ը��֮�󣬸Ͻ�ȥ��������
����·����ɱ�������������ˣ���ô�죿[throw|place]
""")

escape_pod = Room("EscapePod",
"""
\n��������������������ҿ�����ȥû�����Ǻõģ������ǻ�����ˣ���һ����
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