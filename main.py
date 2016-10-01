import webapp2
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment( loader=jinja2.FileSystemLoader('templates'))

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render())

class BioPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('bio.html')
        self.response.out.write(template.render())

class ProjectPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('projects.html')
        self.response.out.write(template.render())

routes = [
    ('/', HomePageHandler),
    ('/bios', BioPageHandler),
    ('/projects', ProjectPageHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)
