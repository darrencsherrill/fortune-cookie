#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookies</h1>"
        fortunes =["you win get freat fortune","do not seek out what will come to you","you always pass the dutchy to the left hand side","1 milloin dollars is in you future","you will live to 100"]
        my_fortune = self.random.choice(fortunes)
        lucky_number = random.randint(1, 999)
        fortune_sentence = "Fortune: " + my_fortune
        number_sentence = "Your lucky number is: " + str(lucky_number)
        number_paragrah = "<p>" + number_sentence + "</p>"
        self.response.write(header + number_paragrah + number_sentence)
        fortune = []
        fortune += ["]


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
