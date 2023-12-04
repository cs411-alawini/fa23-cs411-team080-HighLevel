from flask import Flask, request, jsonify
from flask_cors import CORS

from app.dbop import add_booking, delete_booking, delete_user, detail_search, flight_search, get_booking,insert_user, get_user, login_check, numberbooking, search_airport, searchbooking, update_booking, update_user

app = Flask( __name__)
CORS(app)
app.config['MYSQL_DATABASE_HOST'] = '34.16.2.40'  # Your MySQL host
app.config['MYSQL_DATABASE_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'  # Your MySQL password
app.config['MYSQL_DATABASE_DB'] = 'cs411'  # Your MySQL database name
@app.route('/add_user', methods=['POST'])
def add_user():
    userid = request.json.get('userid')
    password = request.json.get('password')
    # print("WTF")
    # print(request.json)
    # print(request.json.get('userid'))
    # print(userid)
    # print(password)
    # print("WTF")
    response = insert_user(userid, password)
    return response

@app.route('/get_user',methods = ['GET'])
def user_detail():
    userid = request.args.get('userid')
    user = get_user(userid)
    if user is not None:
        return jsonify(user)
    else:
        return "User not found", 404
    
@app.route('/login',methods = ['GET'])
def login():
    userid = request.args.get('userid')
    password = request.args.get('password')
    storepassword = login_check(userid)
    # print("WTFF")
    # print(password)
    # print(storepassword)
    # print("WTFF")
    if storepassword is None:
        return "notfound",404
    if password == storepassword:
        return "success",200
    else :
        return "password not same",406
    
    
    

@app.route('/delete_user', methods=['DELETE'])
def delete_user_route():
    password = request.json.get('password')
    user_id = request.json.get('userid')
    print(password, user_id)
    print(request.json)
    storepassword = login_check(user_id)
    if storepassword is None:
        return "notfound",404
    if password == storepassword:
        delete_user(user_id)
        user = get_user(user_id)
        if user:
            return jsonify({"message": "delete not successfully"}), 405
        else:
             return jsonify({"message": "User deleted successfully"}), 200
    else:
        return "password not same",406
@app.route('/update_user', methods=['PUT'])
def update_user_route():
    password = request.json.get('password')
    newpassword = request.json.get('newpassword')
    user_id = request.json.get('userid')
    storepassword = login_check(user_id)
    print(password,newpassword,user_id,storepassword)
    if storepassword is None:
        return "notfound",404
    if password == storepassword:
        update_user(user_id,newpassword)
        temp = login_check(user_id)
        if temp == newpassword:
            return jsonify({"message": "User update successfully"}), 200
        else:
            return jsonify({"message": "failed to change"}), 404
    else:
        return "password not same",406
    

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
    
    
# booking
@app.route('/add_booking', methods=['POST'])
def Add_Booking():
    json = request.json
    data = json.get('data')
    currentID = numberbooking()
    currentID = currentID + 1
    BOOKING_ID = str(currentID)
    USER_ID = data.get('userid')
    FLIGHT_ID = data.get('flightId')
    print(USER_ID, FLIGHT_ID)
    add_booking(BOOKING_ID,USER_ID,FLIGHT_ID)
    return "booking added",200

@app.route('/get_booking',methods = ['GET'])
def booking_detail():
    data = request.args
    user_id = data.get('user_id')
    booking = get_booking(user_id)
    if booking is not None:
        return jsonify(booking)
    else:
        return "booking not found", 404
@app.route('/delete_booking', methods=['DELETE'])
def delete_booking_route():
    USER_ID = request.json.get('user_id')
    BOOKING_ID = request.json.get('booking_id')
    delete_booking(BOOKING_ID,USER_ID)
    findornot = searchbooking(USER_ID,BOOKING_ID)
    if findornot is None:
        return jsonify({"message": "booking deleted successfully"}), 200
    else:
        return jsonify({"message": "failed"}), 406
    
@app.route('/update_booking/<int:user_id>', methods=['PUT'])
def update_booking_route(user_id):
    BOOKING_ID = request.json.get('username')
    FLIGHT_ID = request.json.get('password')
    updated = update_booking(BOOKING_ID,user_id, FLIGHT_ID)
    return jsonify({"message": "User update successfully"}), 200

@app.route('/search_byairport',methods = ['GET'])
def search_byairport():
    ORIGIN_AIRPORT = request.args.get('ORIGIN_AIRPORT')
    DESTINATION_AIRPORT = request.args.get('DESTINATION_AIRPORT')
    YEAR = request.args.get('YEAR')
    MONTH = request.args.get('MONTH')
    DAY = request.args.get('DAY')
    flight = search_airport(ORIGIN_AIRPORT,DESTINATION_AIRPORT,YEAR,MONTH,DAY)
    
    return jsonify(flight),200 

    
    
    
