#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        x = int(self.request.get("x"))
        options = self.request.get("opt")
        if options == "km":
            self.write(x * 1.60934)
            self.render_template("hello.html")
        elif options == "mei":
            self.write(x * 0.621371)
            self.render_template("hello.html")
        elif options == "fahr":
            self.write(x * 1.8 + 32)
            self.render_template("hello.html")
        elif options == "cel":
            self.write((x -32) / 1.8)
            self.render_template("hello.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
