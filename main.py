import webapp2
from google.appengine.ext import ndb
from random import randrange
quotes = ['Remember computers laugh at us when we do things manually, script everything.','All computers wait at the same speed.','Willyoupleasehelpmefixmykeyboard?Thespacebarisbroken!','A printer consists of three main parts: the case, the jammed paper tray and the blinking red light.']

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers["Content-Type"] = "text/plain"
		self.response.out.write("Hello World....")
		self.response.out.write(quotes[randrange(3)])

app = webapp2.WSGIApplication([('/', MainHandler),],debug=True)

def main():
	app.run()

if __name__ == '__main__':
  main()
