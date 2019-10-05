from flask import Flask, jsonify, request, redirect
from scrapper import News
import sys
import json

app = Flask (__name__)

######################
#       INDEX        #
######################

@app.route ('/', methods=['GET'])
def defaultRoute () :
    return jsonify({
		'author' : 'Developer Student Club, IIT Bhubaneswar',
		'email' : 'amanprtpsingh@gmail.com/adityapal.nghss@gmail.com',
		'endpoint' : 'http://dsciitbbs-newsapi.herokuapp.com',
	    'project_name' : 'IITBBSNewsAPI',
		'project_url' : 'https://github.com/dsciitbbs/iitbbsnewsapi/'
	})

######################
#       NEWS         #
######################

@app.route ('/news', methods=['GET'])
def newsRoute () :
	result = News.getNews()
	return jsonify (result)


######################
#       EVENTS       #
######################

@app.route ('/events', methods=['GET'])
def eventsRoute () :
	result = News.getEvents()
	return jsonify (result)


######################
#       NOTICES      #
######################

@app.route ('/notices', methods=['GET'])
def noticesRoute () :
	result = News.getNotices()
	return jsonify (result)

######################
#       NOTICES      #
######################

@app.route ('/bus', methods=['GET'])
def busRoute () :
	result = News.getBusSchedule()
	return jsonify (result)

@app.route ('/timetable', methods=['GET'])
def timeTable () :
	roll = request.args.get('roll')
	result = News.getTimeTable(roll)
	return jsonify (result)

# Hacky solution for Python 2 :\
@app.route ('/tweets', methods=['GET'])
def tweets () :
	result = News.getTweets()
	if sys.version[0] == 3:
		return jsonify (result)
	else:
		response = app.response_class(
					response=str(result),
					status = 200,
					mimetype='application/json'
				)
		return response

######################
#         404        #
######################
@app.route('/<path:dummy>')
def fallback(dummy):
	return redirect("http://dsciitbbs-newsapi.herokuapp.com")


######################
#    START FLASK     #
######################

if __name__ == "__main__":
	app.run()
