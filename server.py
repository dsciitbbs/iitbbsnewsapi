from flask import Flask, jsonify, request, redirect
from scrapper import News

app = Flask (__name__)

######################
#       INDEX        #
######################

@app.route ('/', methods=['GET'])
def defaultRoute () :
    return jsonify({
		'author' : 'Aman Pratap Singh',
		'email' : 'amanprtpsingh@gmail.com',
		'endpoint' : 'https://iitbbs.herokuapp.com',
	    'project_name' : 'IITBBSNewsAPI',
		'project_url' : 'https://github.com/nightawks/iitbbsnewsapi/'
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

######################
#         404        #
######################
@app.route('/<path:dummy>')
def fallback(dummy):
	return redirect("http://iitbbs.herokuapp.com")


######################
#    START FLASK     #
######################

if __name__ == "__main__":
	app.run()