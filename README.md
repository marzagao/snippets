#Snippets


##Original README

Folks who worked at Google may miss snippets at their current employers. Help is at hand.

Every week, the system emails out a reminder email. Users can reply to it with what they did that week. Users can follow other users via the web, as well as following tags, and assigning tags to themselves. All content matching the tags they follow will be mailed to them in a digest every Monday afternoon. In addition, archives for each user and the most recent data for each tag are visible on the web.

It was hard to make this totally portable. You'll probably want to fork and change the application name and hardcoded email addresses, creating your own application on app engine with authentication restricted to your custom domain. I would love patches to core functionality, though.

Little attention has been paid to making this particularly scalable, but it should work for any small or medium company.

---

###Change's by Harper Reed

* Moved to python2.7
* added bootstrap
* separated out logic into different handlers
* moved to micro framework


####TODO

* migrate away from app engine mail (maybe?)
* make email template based.
