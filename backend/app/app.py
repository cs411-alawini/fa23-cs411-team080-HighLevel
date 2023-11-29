from flask import Flask, request, jsonify

from app.dbop import delete_user, flight_search,insert_user, get_user, update_user

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
        return jsonify(information)
    else:
        return "Flight not found", 404
    
