#coding=gbk

from random import randint

class Scene(object):
	def enter(self):
		print "\n咦，你能看到我吗？快把那个做死的程序员给我拖过来！"
		return "finished"

class Void(Scene):
	def enter(self):
		print "\n呃，你已经进入虚无的时空。。。有程序员要死了！"
		return "finished"

class Hall(Scene):
	def enter(self):
		print "\n大厅里有个外星人在前面，挡住了去军火库的路，怎么办？[shoot|dodge|joke|exit]"
		
		next = raw_input("> ")
		if next == "shoot":
			print "我打，我打。。。没打到，要死了。。。"
			return "death"
		elif next == "dodge":
			print "我闪，我闪。。。哎呀，摔了一跤，要死了。。。"
			return "death"
		elif next == "joke":
			print "嘿，我给你讲个笑话吧，真地很好笑诶，哈哈哈哈"
			print "乘着外星人笑得花枝乱颤的时候。。。我赶紧闪！"
			return "armory"
		elif next == "exit":
			print "8好意思，已经没有退路了"
			return "hall"
		else:
			print "说啥呢"
			return "finished"

class Armory(Scene):
	def enter(self):
		print "\n来到军火库了，不妙，柜子要用密码打开，请输入三位数字密码。"
		print "友情提示，连续输入错误三次，就再也打不开了哈！"
		
		password = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
		
		guesses = 1
		max_guesses = 3
		input = raw_input("> ")
		
		while input != "999" and input != password and guesses < max_guesses:
			print "喂，你到底知不知道？"
			guesses += 1
			input = raw_input("> ")
		
		if guesses < max_guesses:
			print "我靠，这都能猜中，看源码了吧"
			return "bridge"
		else:
			print "哎，明明不知道还要死猜，你当是拍电影啊"
			return "death"	

class Bridge(Scene):
	def enter(self):
		print "\n从军火库拿了炸弹之后，赶紧去往逃生舱"
		print "不料路上又杀出来几个外星人，怎么办？[throw|place]"
		
		next = raw_input("> ")
		if next == "throw":
			print "慌乱之中炸弹爆炸，大家一起去觐见宇宙大帝。。。"
			return "death"
		elif next == "place":
			print "我一边用枪指着炸弹，一边走向逃生舱，然后将炸弹放在门口外"
			print "乘外星人发愣之时，嗖地一下跳出门外并随即关上门，阿门，亲爱的逃生舱我来啦！"
			return "escape_pod"
		else:
			print "说啥呢"
			return "finished"

class EscapePod(Scene):
	def enter(self):
		print "\n舱室内有五个逃生筏，我靠看上去没几个是好的，是死是活看运气了，挑一个吧"
		
		good_id = randint(1, 5)
		
		id = int(raw_input("> "))
		if id == good_id:
			print "走狗屎运啦，拜拜啦，各位可爱的外星人同学！"
			return "finished"
		else:
			print "我靠。。。"
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
