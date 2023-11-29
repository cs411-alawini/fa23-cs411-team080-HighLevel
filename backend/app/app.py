from flask import Flask, request, jsonify

from app.dbop import delete_user, detail_search, flight_search,insert_user, get_user, update_user

app = Flask( __name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    userid = request.json.get('userid')
    username = request.json.get('username')
    password = request.json.get('password')
    insert_user(userid, username, password)
    return "User added",200

@app.route('/get_user/<int:user_id>',methods = ['GET'])
def user_detail(user_id):
    user = get_user(user_id)
    if user is not None:
        return jsonify(user)
    else:
        return "User not found", 404
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    deleted = delete_user(user_id)
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    username = request.json.get('username')
    password = request.json.get('password')
    updated = update_user(user_id,username,password)
    if updated:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

# flight
@app.route('/search_flight',methods = ['GET'])
def search_flight():
    FLIGHT_ID = request.json('FLIGHT_ID')
    FLIGHT_NUMBER = request.json('FLIGHT_NUMBER')
    AIRLINE_IATA = request.json('AIRLINE_IATA')
    TAIL_NUMBER = request.json('TAIL_NUMBER')
    information = flight_search(FLIGHT_ID,FLIGHT_NUMBER,AIRLINE_IATA,TAIL_NUMBER)
    if information is not None:
        return jsonify(information),200
    else:
        return "Flight not found", 404
    
@app.route('/search_detail',methods = ['GET'])
def search_flight():
    FLIGHT_ID = request.json('FLIGHT_ID')
    FLIGHT_NUMBER = request.json('FLIGHT_NUMBER')
    AIRLINE_IATA = request.json('AIRLINE_IATA')
    TAIL_NUMBER = request.json('TAIL_NUMBER')
    
    YEAR = request.json('YEAR')
    MONTH = request.json('MONTH')
    DAY = request.json('DAY')
    DAY_OF_WEEK = request.json('DAY_OF_WEEK')
    SCHEDULED_DEPARTURE = request.json('SCHEDULED_DEPARTURE')
    DEPARTURE_TIME = request.json('DEPARTURE_TIME')
    DEPARTURE_DELAY = request.json('DEPARTURE_DELAY')
    TAXI_OUT = request.json('TAXI_OUT')
    WHEELS_OFF = request.json('WHEELS_OFF')
    SCHEDULED_TIME = request.json('SCHEDULED_TIME')
    ELAPSED_TIME = request.json('ELAPSED_TIME')
    AIR_TIME = request.json('AIR_TIME')
    DISTANCE = request.json('DISTANCE')
    WHEELS_ON = request.json('WHEELS_ON')
    TAXI_IN = request.json('TAXI_IN')
    SCEHDULED_ARRIVAL = request.json('SCEHDULED_ARRIVAL')
    ARRIVAL_TIME = request.json('ARRIVAL_TIME')
    ARRIVAL_DELAY = request.json('ARRIVAL_DELAY')
    DIVERTED = request.json('DIVERTED')
    CANCELED = request.json('CANCELED')
    CANCELLATION_REASON = request.json('CANCELLATION_REASON')
    AIR_SYSTEM_DELAY = request.json('AIR_SYSTEM_DELAY')
    SECURITY_DELAY = request.json('SECURITY_DELAY')
    AIRLINE_DELAY = request.json('AIRLINE_DELAY')
    LATE_AIRCRAFT_DELAY = request.json('LATE_AIRCRAFT_DELAY')
    WEATHER_DELAY = request.json('WEATHER_DELAY')
    ORIGIN_AIRPORT = request.json('ORIGIN_AIRPORT')
    TAIL_NUMBER = request.json('TAIL_NUMBER')
    SCHEDULED_ARRIVAL = request.json('SCHEDULED_ARRIVAL')
    
    information = detail_search(FLIGHT_ID, FLIGHT_NUMBER, YEAR, MONTH, DAY, 
                  DAY_OF_WEEK, SCHEDULED_DEPARTURE, DEPARTURE_TIME, 
                  DEPARTURE_DELAY, TAXI_OUT, WHEELS_OFF, SCHEDULED_TIME, 
                  ELAPSED_TIME, AIR_TIME, DISTANCE, WHEELS_ON, TAXI_IN, 
                  SCHEDULED_ARRIVAL, ARRIVAL_TIME, ARRIVAL_DELAY, DIVERTED, 
                  CANCELED, CANCELLATION_REASON, AIR_SYSTEM_DELAY, 
                  SECURITY_DELAY, AIRLINE_DELAY, LATE_AIRCRAFT_DELAY, 
                  WEATHER_DELAY, ORIGIN_AIRPORT, TAIL_NUMBER)
    if information is not None:
        return jsonify(information),200
    else:
        return "Flight not found", 404
    
