import web
from gothonweb import map

#web.config.debug = False

urls = (
	'/', 'Index',
	'/foo', 'Foo',
	'/hello', 'Hello',
	'/count', 'count',
	'/reset', 'reset',
	'/init', 'InitGame',
	'/game', 'GameEngine'
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store,
		initializer={'count': 0, 'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base='layout')

class Index(object):
	def GET(self):
		greeting = "Hello world!"
		return greeting
		
class Foo(object):
	def GET(self):
		form = web.input(name="BAR")
		return render.foo(bar = form.name)
		
class Hello(object):
	def GET(self):
		return render.hello_form()
		
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
		
class count:
	def GET(self):
		session.count += 1
		return str(session.count)
		
class reset:
	def GET(self):
		session.kill()
		return ""
		
class InitGame(object):
	def GET(self):
		session.room = map.START
		web.seeother("/game")

class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room = session.room)
		else:
			return render.you_died()
			
	def POST(self):
		form = web.input(action=None)
		if session.room and form.action:
			session.room = session.room.go(form.action)
		web.seeother("/game")
		
if __name__ == "__main__":
	app.run()