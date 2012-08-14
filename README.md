Snoop Panther
=============

Snoop Panther was inspired by [Keith Casey](http://caseysoftware.com/) at [That Conference](http://www.thatconference.com/) on August 13, 2012. It is a method of quickly acquiring information about the people you meet.

You can do as you please with this software, but I would appreciate if you'd let me know your thoughts if you end up deploying; and if you end up enhancing that you highly consider a pull request.

### How to deploy and use
* Create an App Engine account
* Add your app's name to ```index.yaml```
* Create a Twilio account. Configure it to forward SMS messages to your base App Engine URL as POST
* Create a Full Contact account and copy your API key to ```main.py```
* Configure the other constant variables per your preference
* Configure the ```templates/email.html``` template to your liking
* Deploy and send a text message with an email address to your Twilio number
* Check your email
* ...
* Profit
