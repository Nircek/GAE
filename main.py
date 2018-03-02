#!/usr/bin/python
# -*- coding: UTF-8 -*-
import webapp2

class MainPage(webapp2.RequestHandler):
    def w(self,x):
        """Write to response"""
        self.response.write(x)
    def v(self,x):
        """get Variable"""
        return self.request.params[x];
    def wv(self,x):
        """Write Variable to response"""
        self.w(self.v(x))
    def ie(self,x):
        """If Exist variable in params"""
        if x in self.request.params:
            return True
        else:
            return False
    def post(self):
        self.get()
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        #-#-#-#-#
        def w(x):
            self.w(x)
        def v(x):
            return self.v(x)
        def wv(x):
            self.wv(x)
        def ie(x):
            return self.ie(x)
        #-#-#-#-#
        w('Hello world!')
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
