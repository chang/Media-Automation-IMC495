import twilio
from API_KEYS import ACCOUNT_SID, AUTH_TOKEN 
from twilio.rest import TwilioRestClient

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


class Subscriber:
	def __init__(self):
		self.subscribers = {}


	def opt_in(self, from_):
		self.subscribers[from_] = 1


	def opt_out(self, from_):
		self.subscribers[from_] = 0


	def message_subscribers(self, msg):
		for phone, status in self.subscribers.items():
			if status == 1:
				client.messages.create(
				    to = phone,
				    from_ = '+12244123104',
				    body = msg
				)


