""" Running a simple flask program """
# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for thr the root URL ("/")
@app.route("/")
def hello_world():
    # Function that handles requests to the root URL
    return {"message" : "Hello World"}
