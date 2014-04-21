import logging

from google.appengine.api import mail
from google.appengine.api import taskqueue

from dateutil import *
from model import *

from django.conf import settings

from utilities import framework

REMINDER = """
Hullo fellow colleague,

Please reply by Monday afternoon with an answer to the following two questions:

1. What were the most important tasks you or your team worked on last week? Any results you'd like to share?
2. What do you or your team intend on working this week?

Aim for short sentences and scannable text. Bullet points are preferable over prose.

On Monday night (11pm), you should receive the snippets digest e-mail.
"""

class ReminderEmail(framework.BaseHandler):
    def get(self):
        all_users = User.all().filter("enabled =", True).fetch(500)
        for user in all_users:
            # TODO: Check if one has already been submitted for this period.
            taskqueue.add(url='/onereminder', params={'email': user.email})


class OneReminderEmail(framework.BaseHandler):
    def post(self):
        mail.send_mail(sender="snippets <" + settings.SITE_EMAIL + ">",
                       to=self.request.get('email'),
                       subject="Snippet time!",
                       body=REMINDER)

    def get(self):
        self.post()


class DigestEmail(framework.BaseHandler):
    def get(self):
        all_users = User.all().filter("enabled =", True).fetch(500)
        for user in all_users:
            taskqueue.add(url='/onedigest', params={'email': user.email})


class OneDigestEmail(framework.BaseHandler):
    def __send_mail(self, recipient, body):
        mail.send_mail(sender="snippets <" + settings.SITE_EMAIL + ">",
                       to=recipient,
                       subject="Snippet digest delivery!",
                       body=body)

    def __snippet_to_text(self, snippet):
        divider = '-' * 30
        return '%s\n%s\n%s' % (snippet.user.pretty_name(), divider, snippet.text)

    def get(self):
        self.post()

    def post(self):
        user = user_from_email(self.request.get('email'))
        d = date_for_retrieval()
        all_snippets = Snippet.all().filter("date =", d).fetch(500)
        all_users = User.all().fetch(500)
        following = compute_following(user, all_users)
        logging.info(all_snippets)
        body = '\n\n\n'.join([self.__snippet_to_text(s) for s in all_snippets if s.user.email in following])
        if body:
            self.__send_mail(user.email, 'https://' + settings.SITE_DOMAIN + '\n\n' + body)
        else:
            logging.info(user.email + ' not following anybody.')
