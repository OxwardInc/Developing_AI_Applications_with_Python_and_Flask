"""Creating a simple flask application"""
# Import the Flask class from the flask module
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the ame of the current module
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route("/")
def index():
    """
    Generating a simple function
    """
    # Function that handles requests to the root URL
    # Return a plain text response
    return 'hello world'

@app.route("/no_content")
def no_content():
    """
    Return 'No content found' with a status of 204
    """
    return ({"message" : "No content found"}, 204)

@app.route("/exp")
def index_explicit():
    '''
    Using the make_response() method
    '''
    resp = make_response({"message" : 'Using make response'})
    resp.status_code = 200
    return resp
