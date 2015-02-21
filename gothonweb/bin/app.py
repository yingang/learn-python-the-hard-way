import web

web.config.debug = False

urls = (
	'/', 'Index',
	'/foo', 'Foo',
	'/hello', 'Hello',
	'/count', 'count',
	'/reset', 'reset'
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count': 0})

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

if __name__ == "__main__":
	app.run()