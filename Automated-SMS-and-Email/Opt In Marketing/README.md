To run the Flask server for receiving SMS messages using Twilio:

1. Build **server.py**.
2. Expose the port by running `ngrok http 5000` from a terminal.
3. Update Twilio Incoming Messages webhook URL to the ngrok URL (something like http://ebddd06b.ngrok.io)