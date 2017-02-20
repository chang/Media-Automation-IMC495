from flask import Flask, request
from twilio_helpers import twiml_response, survey_invitation, parse_request
from Subscriber import Subscriber

app = Flask(__name__)

database = Subscriber()


# Twilio configured incoming message handler
@app.route('/twilio', methods=['POST', 'GET'])
def message():
	if request.method == "POST":
		from_, body = parse_request(request)

		if body.lower().startswith('yes'):
			database.opt_in(from_)
			return twiml_response("Thanks for opting in! Text STOP to this number anytime to unsubscribe.")
		elif body.lower().startswith('stop'):
			database.opt_out(from_)
			return twiml_response("You've been unsubscribed from the IMC490 newsletter.")
		else:
			return twiml_response("Yep, Twilio is working as it should!")


	elif request.method == "GET":
		return "Hello from the twilio message handler!"


@app.route('/subscribers', methods=['GET'])
def subscribers_page():
	out = ""
	for phone,status in database.subscribers.items():
		out += str(phone) + "  " + str(status) + "\n"
	return out


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == "POST":
		# If we get a POST request, return a TwiML formatted instruction
		print("We got a POST request!")
		print(request.form)
		twiml_response = "<Response><Message> This is an automated response.</Message></Response>"
		return twiml_response
	elif request.method == "GET":
		print("We got a GET request!")

	return "Hello twilio!"





if __name__ == "__main__":
	app.run()