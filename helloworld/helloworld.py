#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.wsgi

import wsgiref.simple_server
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
#Hey i am in your code!

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("80% for Machine Learning")

class SalinggaHandler(tornado.web.RequestHandler):
    def get(self):
        x = 5
        y = 5
        self.write("I don't know what this is %f" % (x*y))

    # tornado.options.parse_command_line()
class JingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
             title="processes",
             header="PROCESS",
             steps=[
                 "DATA MINING",
                 "DATA CLEANING",
                 "ANALYSIS",
                 "DATA VISUALIZATION"
             ]
        )
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/salingga", SalinggaHandler),
    (r"/jing", JingHandler),
])

application = tornado.wsgi.WSGIAdapter(application)
