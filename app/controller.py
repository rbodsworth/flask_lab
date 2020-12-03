from flask import render_template, request 
from app import app
from app.models.event_list import events, add_new_event
from event import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events ) 

@app.route('/add-event', methods=['POST'])
def add_event():

    eventTitle = request.form['title']
    eventDesc = request.form['description']
    newEvent = Events(title=eventTitle, description=eventDesc, done=False)
    add_new_event(newEvent)
    return render_template('index.html', title='Home', events=events)
  