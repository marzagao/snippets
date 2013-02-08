import webapp2
from handlers import site
from handlers import emails
"""
                      __
_______  ____  __ ___/  |_  ____   ______
\_  __ \/  _ \|  |  \   __\/ __ \ /  ___/
 |  | \(  <_> )  |  /|  | \  ___/ \___ \
 |__|   \____/|____/ |__|  \___  >____  >
                               \/     \/
"""


API = []

SITE =  [
    ('/', site.MainHandler),
    ('/user/(.*)', site.UserHandler),
    ('/tag/(.*)', site.TagHandler),
    ('/follow', site.FollowHandler),
    ('/unfollow', site.UnfollowHandler),
    ('/reminderemail', emails.ReminderEmail),
    ('/digestemail', emails.DigestEmail),
    ('/onereminder', emails.OneReminderEmail),
    ('/onedigest', emails.OneDigestEmail),
]

ADMIN = []

ROUTES = []
ROUTES.extend(SITE)
ROUTES.extend(ADMIN)
ROUTES.append(webapp2.Route(r'/.*$', site.NotFoundHandler))
