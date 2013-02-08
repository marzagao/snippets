import os
import sys

from django.conf import settings

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'contrib'))

import appengine_config

from routes import ROUTES

import webapp2

"""
               .__
  _____ _____  |__| ____
 /     \\__  \ |  |/    \
|  Y Y  \/ __ \|  |   |  \
|__|_|  (____  /__|___|  /
      \/     \/        \/

"""

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': settings.SESSION_SECRET_KEY,
}

application = webapp2.WSGIApplication(ROUTES, config=config, debug=settings.DEBUG)

"""
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()

"""
