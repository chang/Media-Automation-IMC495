def twiml_response(msg):
	"""
	returns a TwiML formatted instruction to SMS the message mg
	"""
	return "<Response><Message>" + str(msg) + "</Message></Response>"


def parse_request(request):
	"""
	returns tuple of message data in form:
	(from phone number, body text)
	"""
	return (request.form['From'], request.form['Body'])


def survey_invitation():
	pass