import json

from flask import jsonify, request_started, Flask, request
from service import service

app = Flask(__name__)

DEFAULT_STATUS_CODE = "failure"
SUCCESS_STATUS_CODE = "success"

@app.route('/')
def greet():
    return 'Welcome to Python Assignment'

@app.route('/assignment/sample-bookings', methods=['GET'])
def handle_request():
    """
    API endpoint for fetching all bookings
    """
    response = prepare_result_container()
    try:
        response["response"] = service.fetch_sample_bookings()
        response["status"] = SUCCESS_STATUS_CODE
    except Exception as error:
        response["error"] = str(error)
        return json.dumps(response)
    else:
        return json.dumps(response)

def prepare_result_container():
    """
    Returns a dict - response
    """
    return {
        "response":{},
        "status":DEFAULT_STATUS_CODE,
        "error": ""
    }


@app.route('/getData', methods=['POST'])
def findData():
    data = jsonify(request.json)
    for index in data:
        for key in data[index]:
            capacity = data[index][key]
            startTime = data[index][key]
            endTime = data[index][key]
            AvailableHalls = service.search(capacity , startTime , endTime , index)
            print(AvailableHalls,"ldkkfd")
            return {
                "response":AvailableHalls,
                "status":SUCCESS_STATUS_CODE,
                "error": ""
                
            }
        

   {
    "0": {
        "capacity": 50,
        "startTime": "2020-12-27 15:00:00",
        "endTime": "2020-12-27 16:00:00"
    },
    "1": {
        "capacity": 1000,
        "startTime": "2020-12-27 15:00:00",
        "endTime": "2020-12-27 17:00:00"
    }
}

    


    # {"id": "2546543", "hallName": "A", "capacity": 50, "startDate": "2021-06-27 15:00:00", "endDate": "2021-06-27 16:00:00"}




"""
Input

{
    "0": {
        "capacity": 50,
        "startTime": "2020-12-27 15:00:00",
        "endTime": "2020-12-27 16:00:00"
    },
    "1": {
        "capacity": 1000,
        "startTime": "2020-12-27 15:00:00",
        "endTime": "2020-12-27 17:00:00"
    }
}
 

Output

{
    "0" : ["B", "C", "D", "E", "F"],
    "1" : ["F"]
}
"""