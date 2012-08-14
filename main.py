#!/usr/bin/env python

import webapp2
import jinja2
import os
import simplejson as json
from google.appengine.api import mail, urlfetch

FC_KEY = 'TODO'
FC_URL = 'https://api.fullcontact.com/v2/person.json?email=%s&apiKey=%s'
TEMPLATES_DIR = 'templates'
SUBJECT_PREFIX = 'Snoop Panther: '
FROM_EMAIL = 'TODO'
TO_EMAIL = 'TODO'
EMAIL_TEMPLATE = 'email.html'

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__),
            TEMPLATES_DIR,
        )
    )
)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        """
        Handle the GET request. Eg browser
        """
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

    def post(self):
        """
        Workhorse when Twilio receives a SMS
        """
        lookup_email = self.request.get('Body')
        request_url = FC_URL % (lookup_email, FC_KEY)
        result = urlfetch.fetch(request_url)
        content = json.loads(result.content)

        template = jinja_environment.get_template(EMAIL_TEMPLATE)
        email_body = template.render(content)

        mail.send_mail(sender=FROM_EMAIL,
                to=TO_EMAIL,
                subject=SUBJECT_PREFIX + lookup_email,
                body=email_body,
                html=email_body)

        self.response.write('')

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
