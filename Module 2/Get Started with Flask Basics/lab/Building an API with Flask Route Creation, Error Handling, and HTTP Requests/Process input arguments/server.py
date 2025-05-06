"""Process input arguments"""

from flask import Flask, make_response, jsonify, request
import data
from data import data
app = Flask(__name__)

@app.route("/data")
def get_data():
    '''Trying to get the users data from the data.py file'''
    try:
        # Check if 'data' exists and has a length greater tan 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the lenght of tha data
            response = make_response(jsonify({"message": f"Data of length {len(data)} found"}))
            response.status_code = 200
            return response
        else:
            # If 'data' is empty, return a JSON response with 500 Internal Server error status code
            response = make_response(jsonify({"message": "Data is empty"}))
            response.status_code = 500
            return response
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not found status code
        response = make_response(jsonify({"message": "Data not found"}))
        response.status_code = 404
        return response


@app.route("/name_search")
def name_search():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        422: If argument 'q' is missing
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    # Check if the query parameter 'q' is missing
    if not query:
        # Return a JSON response with a message indicating 'q' is missging and a 422 Unprocessable Entity status 
        # code
        response = make_response(jsonify({"message" : "Query parameter 'q' is missing"}))
        response.status_code = 422
        return response
     # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person
    
    # If no match is found, return a JSON response with a message indicating the person was not found 
    # and a 404 Not Found status code
    response = make_response(jsonify({"message": 'Person not found'}))
    response.status_code = 404
    return response

@app.route("/count")
def count():
    """Creating a count endpoint
    """
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        # Replace {insert code to find length of data} with len(data) to get the length of the 'data' collection
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if person["id"] == str(id):
            # Return the matching person as a JSON response with a 200 OK status code
            return person
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return {"message": "person not found"}, 404
@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if person["id"] == str(id):
            # Remove the person from the 'data' list
            data.remove(person)
            # Return a JSON response with a message confirming deletion and a 200 OK status code
            return {"message": f"Person with ID {id} deleted"}, 200
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return {"message": "person not found"}, 404