#!/usr/bin/python
# -*- coding: UTF-8 -*-
# file from https://github.com/Nircek/GAE
# licensed under MIT license

# MIT License

# Copyright (c) 2018 Nircek

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
