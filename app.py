from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server GateWay Interface) application.

'''



### WSGI application


app=Flask(__name__)

@app.route("/")

def welcome():
  return "Welcome to this Flask course . This should be an amazing course !!. Thank you"


@app.route("/index")

def index():
  return "Welcome to the index page"



if __name__=="__main__":
  app.run(debug=True)