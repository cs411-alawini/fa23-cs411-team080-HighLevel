from flask import Flask, request, jsonify

from app.dbop import delete_user, detail_search, flight_search,insert_user, get_user, update_user

app = Flask( __name__)
app.config['MYSQL_DATABASE_HOST'] = '34.16.2.40'  # Your MySQL host
app.config['MYSQL_DATABASE_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'  # Your MySQL password
app.config['MYSQL_DATABASE_DB'] = 'cs411'  # Your MySQL database name
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
        return jsonify({"message": "User update successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

# flight
@app.route('/search_flight',methods = ['GET'])
def search_flight():
    FLIGHT_ID = request.args.get('FLIGHT_ID')
    FLIGHT_NUMBER = request.args.get('FLIGHT_NUMBER')
    AIRLINE_IATA = request.args.get('AIRLINE_IATA')
    TAIL_NUMBER = request.args.get('TAIL_NUMBER')
    information = flight_search(FLIGHT_ID,FLIGHT_NUMBER,AIRLINE_IATA,TAIL_NUMBER)
    if information is not None:
        return jsonify(information),200
    else:
        return "Flight not found", 404
    
@app.route('/search_detail',methods = ['GET'])
def search_detail():
    FLIGHT_ID = request.args.get('FLIGHT_ID')
    FLIGHT_NUMBER = request.args.get('FLIGHT_NUMBER')
    AIRLINE_IATA = request.args.get('AIRLINE_IATA')
    TAIL_NUMBER = request.args.get('TAIL_NUMBER')
    
    YEAR = request.args.get('YEAR')
    MONTH = request.args.get('MONTH')
    DAY = request.args.get('DAY')
    DAY_OF_WEEK = request.args.get('DAY_OF_WEEK')
    SCHEDULED_DEPARTURE = request.args.get('SCHEDULED_DEPARTURE')
    DEPARTURE_TIME = request.args.get('DEPARTURE_TIME')
    DEPARTURE_DELAY = request.args.get('DEPARTURE_DELAY')
    TAXI_OUT = request.args.get('TAXI_OUT')
    WHEELS_OFF = request.args.get('WHEELS_OFF')
    SCHEDULED_TIME = request.args.get('SCHEDULED_TIME')
    ELAPSED_TIME = request.args.get('ELAPSED_TIME')
    AIR_TIME = request.args.get('AIR_TIME')
    DISTANCE = request.args.get('DISTANCE')
    WHEELS_ON = request.args.get('WHEELS_ON')
    TAXI_IN = request.args.get('TAXI_IN')
    SCEHDULED_ARRIVAL = request.args.get('SCEHDULED_ARRIVAL')
    ARRIVAL_TIME = request.args.get('ARRIVAL_TIME')
    ARRIVAL_DELAY = request.args.get('ARRIVAL_DELAY')
    DIVERTED = request.args.get('DIVERTED')
    CANCELED = request.args.get('CANCELED')
    CANCELLATION_REASON = request.args.get('CANCELLATION_REASON')
    AIR_SYSTEM_DELAY = request.args.get('AIR_SYSTEM_DELAY')
    SECURITY_DELAY = request.args.get('SECURITY_DELAY')
    AIRLINE_DELAY = request.args.get('AIRLINE_DELAY')
    LATE_AIRCRAFT_DELAY = request.args.get('LATE_AIRCRAFT_DELAY')
    WEATHER_DELAY = request.args.get('WEATHER_DELAY')
    ORIGIN_AIRPORT = request.args.get('ORIGIN_AIRPORT')
    TAIL_NUMBER = request.args.get('TAIL_NUMBER')
    SCHEDULED_ARRIVAL = request.args.get('SCHEDULED_ARRIVAL')
    
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
    
