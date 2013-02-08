import email
import re

from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from django.conf import settings

from dateutil import date_for_new_snippet
from model import user_from_email, create_or_replace_snippet

import webapp2


class ReceiveEmail(InboundMailHandler):
    """Receive a snippet email and create or replace snippet for this week."""

    def receive(self, message):
        user = user_from_email(email.utils.parseaddr(message.sender)[1])
        for content_type, body in message.bodies('text/plain'):
            # http://stackoverflow.com/questions/4021392/how-do-you-decode-a-binary-encoded-mail-message-in-python
            if body.encoding == '8bit':
                body.encoding = '7bit'
            content = body.decode()

            sig_pattern = re.compile(r'^\-\-\s*$', re.MULTILINE)
            split_email = re.split(sig_pattern, content)
            content = split_email[0]

            reply_pattern = re.compile(r'^On.*at.*snippets', re.MULTILINE)
            split_email = re.split(reply_pattern, content)
            content = split_email[0]

            create_or_replace_snippet(user, content, date_for_new_snippet())

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': settings.SESSION_SECRET_KEY,
}

application = webapp2.WSGIApplication([ReceiveEmail.mapping()], config=config, debug=settings.DEBUG)

