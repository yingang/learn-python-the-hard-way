class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

lyrics = ["happy birthday to you",
	"I don't want to get sued",
	"so I'll stop right there"]
			
happy_bday = Song(lyrics)

lyrics = ["they rally around the family",
	"with pockets full of shells"]

bulls_on_parade = Song(lyrics)
				
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
