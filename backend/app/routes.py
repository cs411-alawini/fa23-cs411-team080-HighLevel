from flask import Blueprint, request, jsonify

from app.dbop import delete_user,insert_user, get_user, update_user

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/add_user', methods=['POST'])
def add_user():
    userid = request.json.get('userid')
    username = request.json.get('username')
    password = request.json.get('password')
    insert_user(userid, username, password)
    return "User added",201

@bp.route('/get_user/<int:user_id>',method = ['GET'])
def user_detail(user_id):
    user = get_user(user_id)
    if user is not None:
        return jsonify(user)
    else:
        return "User not found", 404
@bp.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    deleted = delete_user(user_id)
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
@bp.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    username = request.json.get('username')
    password = request.json.get('password')
    updated = update_user(user_id,username,password)
    if updated:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404