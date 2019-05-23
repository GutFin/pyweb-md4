from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/styles.css")
def styles_css():
    return static_file("styles.css", root="")
    
@route("/")
@view("predictions")
def index():
 now = dt.now()


 return {
   "date": f"{now.year}-{now.month}-{now.day}",
   "predictions": generate_prophecies(),
 }

@route("/api/forecasts")
def api_test():
   return {"test_passed": True}

run(
 host="localhost",
 port=8080,
 autoreload=True
)