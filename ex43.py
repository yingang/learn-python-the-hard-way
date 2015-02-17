#coding=gbk

from random import randint

class Scene(object):
	def enter(self):
		print "\n�ף����ܿ������𣿿���Ǹ������ĳ���Ա�����Ϲ�����"
		return "finished"

class Void(Scene):
	def enter(self):
		print "\n�������Ѿ��������޵�ʱ�ա������г���ԱҪ���ˣ�"
		return "finished"

class Hall(Scene):
	def enter(self):
		print "\n�������и���������ǰ�棬��ס��ȥ������·����ô�죿[shoot|dodge|joke|exit]"
		
		next = raw_input("> ")
		if next == "shoot":
			print "�Ҵ��Ҵ򡣡���û�򵽣�Ҫ���ˡ�����"
			return "death"
		elif next == "dodge":
			print "������������������ѽ��ˤ��һ�ӣ�Ҫ���ˡ�����"
			return "death"
		elif next == "joke":
			print "�٣��Ҹ��㽲��Ц���ɣ���غܺ�Ц������������"
			print "����������Ц�û�֦�Ҳ���ʱ�򡣡����ҸϽ�����"
			return "armory"
		elif next == "exit":
			print "8����˼���Ѿ�û����·��"
			return "hall"
		else:
			print "˵ɶ��"
			return "finished"

class Armory(Scene):
	def enter(self):
		print "\n����������ˣ��������Ҫ������򿪣���������λ�������롣"
		print "������ʾ����������������Σ�����Ҳ�򲻿��˹���"
		
		password = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
		
		guesses = 1
		max_guesses = 3
		input = raw_input("> ")
		
		while input != "999" and input != password and guesses < max_guesses:
			print "ι���㵽��֪��֪����"
			guesses += 1
			input = raw_input("> ")
		
		if guesses < max_guesses:
			print "�ҿ����ⶼ�ܲ��У���Դ���˰�"
			return "bridge"
		else:
			print "����������֪����Ҫ���£��㵱���ĵ�Ӱ��"
			return "death"	

class Bridge(Scene):
	def enter(self):
		print "\n�Ӿ��������ը��֮�󣬸Ͻ�ȥ��������"
		print "����·����ɱ�������������ˣ���ô�죿[throw|place]"
		
		next = raw_input("> ")
		if next == "throw":
			print "����֮��ը����ը�����һ��ȥ��������ۡ�����"
			return "death"
		elif next == "place":
			print "��һ����ǹָ��ը����һ�����������գ�Ȼ��ը�������ſ���"
			print "�������˷��֮ʱ��ವ�һ���������Ⲣ�漴�����ţ����ţ��װ�����������������"
			return "escape_pod"
		else:
			print "˵ɶ��"
			return "finished"

class EscapePod(Scene):
	def enter(self):
		print "\n��������������������ҿ�����ȥû�����Ǻõģ������ǻ�����ˣ���һ����"
		
		good_id = randint(1, 5)
		
		id = int(raw_input("> "))
		if id == good_id:
			print "�߹�ʺ�������ݰ�������λ�ɰ���������ͬѧ��"
			return "finished"
		else:
			print "�ҿ�������"
			return "death"
	
class Death(Scene):
	def enter(self):
		print "GAME OVER~~"
		return "finished"

class Map(object):

	map_list = {
		"hall" : Hall(),
		"armory" : Armory(),
		"bridge" : Bridge(),
		"escape_pod" : EscapePod(),
		"death" : Death()
		}
	
	def get_init_map(self):
		return self.map_list["hall"]
		
	def get_map(self, map_name):
		if map_name in self.map_list:
			return self.map_list[map_name]
		else:
			return Void()

class Game(object):

	def play(self):
		current_map = Map().get_init_map()
		
		while True:
			next_map = current_map.enter()

			if next_map == "finished":
				print "\n"
				break
				
			current_map = Map().get_map(next_map)

Game().play()
