import apiai
import os
import json
from termcolor import cprint 
def send_ai_request(message):
	cprint(message, 'green')
	API_AI_CLIENT_ACCESS_TOKEN = os.environ["APIAI_KEY"]
	ai = apiai.ApiAI(API_AI_CLIENT_ACCESS_TOKEN)
	ai_request = ai.text_request()
	ai_request.lang = 'en'  # optional, default value equal 'en'
	ai_request.query = message
	ai_response = json.loads(ai_request.getresponse().read())
	#cprint(json.dumps(ai_response, indent=4), "magenta")
	return ai_response["result"]["action"], ai_response["result"]["parameters"]

def handle_response(t):
	action, parameters = t
	if action == "show_office":
		cprint("%s is at HK island." % (parameters["office"]), "red", "on_white")
	if action == "show_proglang":
		cprint("%s is a programming language" % (parameters["proglang"]), "blue", "on_white")
	if action == "show_person":
		cprint("%s is my friend." % (parameters["person"]), "cyan", "on_white")

handle_response(send_ai_request("Where is OneSky office?"))
handle_response(send_ai_request("Who is David?"))
handle_response(send_ai_request("What is Java?"))
