from flask import jsonify
from pymysql import IntegrityError
from app.db import get_db

def insert_user(userid, password):
    db = get_db()
    cursor = db.cursor()
    try:
        query = "INSERT INTO User (USER_ID, PASSWORD) VALUES ('{}', '{}')".format(userid, password)
        cursor.execute(query)
        db.commit()
        return jsonify({"message": "User added"}), 200
    except IntegrityError:
        return jsonify({"message": "User ID already exists"}), 409
    finally:
        cursor.close()
        
def login_check(userid):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT PASSWORD FROM User WHERE USER_ID = '{}'".format(userid)
    cursor.execute(query)
    password = cursor.fetchone()
    cursor.close()
    return password[0]
    
def get_user(user_id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM User WHERE USER_ID = '{}'".format(user_id)
    cursor.execute(query)
    user = cursor.fetchall()
    cursor.close()
    return user
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM User WHERE USER_ID = '{}'".format(user_id)
    cursor.execute(query)
    db.commit()
    cursor.close()
def update_user(userid, password):
    db = get_db()
    cursor = db.cursor()
    
    query = "UPDATE User SET PASSWORD = '{}' WHERE USER_ID = '{}'".format(password, userid)
    cursor.execute(query)
    db.commit()
    cursor.close()
def flight_search(FLIGHT_ID=None,FLIGHT_NUMBER=None,AIRLINE_IATA=None,TAIL_NUMBER=None):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Flight WHERE 1=1 "
    if FLIGHT_ID :
        
        query += "AND FLIGHT_ID = {}".format(FLIGHT_ID)
    else:
        if FLIGHT_NUMBER:
            query += "AND FLIGHT_NUMBER = {}".format(FLIGHT_NUMBER)
        if AIRLINE_IATA:
            query += "AND AIRLINE_IATA = {}".format(AIRLINE_IATA)
        if TAIL_NUMBER:
            query += "AND TAIL_NUMBER = {}".format(TAIL_NUMBER)
    cursor.execute(query)
    flightinformation = cursor.fetchall()
    cursor.close()
    return flightinformation
def detail_search(FLIGHT_ID=None, FLIGHT_NUMBER=None, YEAR=None, MONTH=None, DAY=None, 
                  DAY_OF_WEEK=None, SCHEDULED_DEPARTURE=None, DEPARTURE_TIME=None, 
                  DEPARTURE_DELAY=None, TAXI_OUT=None, WHEELS_OFF=None, SCHEDULED_TIME=None, 
                  ELAPSED_TIME=None, AIR_TIME=None, DISTANCE=None, WHEELS_ON=None, TAXI_IN=None, 
                  SCHEDULED_ARRIVAL=None, ARRIVAL_TIME=None, ARRIVAL_DELAY=None, DIVERTED=None, 
                  CANCELED=None, CANCELLATION_REASON=None, AIR_SYSTEM_DELAY=None, 
                  SECURITY_DELAY=None, AIRLINE_DELAY=None, LATE_AIRCRAFT_DELAY=None, 
                  WEATHER_DELAY=None, ORIGIN_AIRPORT=None, TAIL_NUMBER=None):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Flight WHERE 1=1 "
    if FLIGHT_ID :
        query += "AND FLIGHT_ID = {}".format(FLIGHT_ID)
    else:
        query = "SELECT * FROM Flight JOIN Trip on Flight.FLIGHT_ID = Trip.FLIGHT_ID WHERE 1=1"
        if FLIGHT_NUMBER:
            query += "AND FLIGHT_NUMBER = {}".format(FLIGHT_NUMBER)
        if YEAR:
            query += "AND YEAR = {}".format(YEAR)
        if TAIL_NUMBER:
            query += "AND TAIL_NUMBER = {}".format(TAIL_NUMBER)
            
        if MONTH:
            query += "AND MONTH = {}".format(MONTH)
        if DAY:
            query += "AND DAY = {}".format(DAY)
        if DAY_OF_WEEK:
            query += "AND DAY_OF_WEEK = {}".format(DAY_OF_WEEK)
            
        if SCHEDULED_DEPARTURE:
            query += "AND SCHEDULED_DEPARTURE = {}".format(SCHEDULED_DEPARTURE)
        if DEPARTURE_TIME:
            query += "AND DEPARTURE_TIME = {}".format(DEPARTURE_TIME)
        if DEPARTURE_DELAY:
            query += "AND DEPARTURE_DELAY = {}".format(DEPARTURE_DELAY)
            
        if TAXI_OUT:
            query += "AND TAXI_OUT = {}".format(TAXI_OUT)
        if WHEELS_OFF:
            query += "AND WHEELS_OFF = {}".format(WHEELS_OFF)
        if SCHEDULED_TIME:
            query += "AND SCHEDULED_TIME = {}".format(SCHEDULED_TIME)
            
        if ELAPSED_TIME:
            query += "AND ELAPSED_TIME = {}".format(ELAPSED_TIME)
        if AIR_TIME:
            query += "AND AIR_TIME = {}".format(AIR_TIME)
        if DISTANCE:
            query += "AND DISTANCE = {}".format(DISTANCE)
            
            
        if WHEELS_ON:
            query += "AND WHEELS_ON = {}".format(WHEELS_ON)
        if TAXI_IN:
            query += "AND TAXI_IN = {}".format(TAXI_IN)
        if SCHEDULED_ARRIVAL:
            query += "AND SCHEDULED_ARRIVAL = {}".format(SCHEDULED_ARRIVAL)    
            
        if ARRIVAL_TIME:
            query += "AND ARRIVAL_TIME = {}".format(ARRIVAL_TIME)
        if ARRIVAL_DELAY:
            query += "AND ARRIVAL_DELAY = {}".format(ARRIVAL_DELAY)
        if DIVERTED:
            query += "AND DIVERTED = {}".format(DIVERTED)    
            
        if CANCELED:
            query += "AND CANCELED = {}".format(CANCELED)
        if CANCELLATION_REASON:
            query += "AND CANCELLATION_REASON = {}".format(CANCELLATION_REASON)
        if AIR_SYSTEM_DELAY:
            query += "AND AIR_SYSTEM_DELAY = {}".format(AIR_SYSTEM_DELAY)    
            
        if SECURITY_DELAY:
            query += "AND SECURITY_DELAY = {}".format(SECURITY_DELAY)
        if AIRLINE_DELAY:
            query += "AND AIRLINE_DELAY = {}".format(AIRLINE_DELAY)
        if LATE_AIRCRAFT_DELAY:
            query += "AND LATE_AIRCRAFT_DELAY = {}".format(LATE_AIRCRAFT_DELAY)    
            
            
        if WEATHER_DELAY:
            query += "AND WEATHER_DELAY = {}".format(WEATHER_DELAY)
        if ORIGIN_AIRPORT:
            query += "AND ORIGIN_AIRPORT = {}".format(ORIGIN_AIRPORT)
            
    cursor.execute(query)
    flightinformation = cursor.fetchone()
    cursor.close()
    return flightinformation

def add_booking(BOOKING_ID,USER_ID,FLIGHT_ID,BOOKED_NUMBER):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO Booking (BOOKING_ID, USER_ID, FLIGHT_ID,BOOKED_NUMBER) VALUES ('{}', '{}', '{}')".format(BOOKING_ID,USER_ID,FLIGHT_ID,BOOKED_NUMBER)
    cursor.execute(query)
    db.commit()
    cursor.close()
    
def delete_booking(BOOKING_ID,USER_ID):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Booking WHERE USER_ID = '{}' AND BOOKING_ID = '{}'".format(USER_ID,BOOKING_ID)
    cursor.execute(query)
    db.commit()
    cursor.close()
def get_booking(USER_ID):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Booking WHERE USER_ID = '{}'".format(USER_ID)
    cursor.execute(query)
    booking = cursor.fetchall()
    cursor.close()
    return booking
def update_booking(BOOKING_ID,USER_ID, FLIGHT_ID,BOOKED_NUMBER):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE Booking SET BOOKED_NUMBER = '{}' WHERE USER_ID = '{}' AND BOOKING_ID = '{}'".format(BOOKED_NUMBER, USER_ID, BOOKING_ID)
    cursor.execute(query)
    db.commit()
    cursor.close()
def search_airport(ORIGIN_AIRPORT,DESTINATION_AIRPORT,YEAR,MONTH,DAY):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM ToAndFrom JOIN Trip on Trip.FLIGHT_ID = ToAndFrom.FLIGHT_ID WHERE ToAndFrom.ORIGIN_AIRPORT = '{}' AND ToAndFrom.DESTINATION_AIRPORT = '{}'".format(ORIGIN_AIRPORT,DESTINATION_AIRPORT)
    cursor.execute(query),
    airport = cursor.fetchall()
    cursor.close()
    return airport
def numberbooking():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT(*) FROM Booking"
    cursor.execute(query),
    number = cursor.fetchone()
    cursor.close()
    return number[0]
def searchbooking(USER_ID,BOOKING_ID):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Booking WHERE USER_ID = '{}' AND BOOKING_ID = '{}'".format(USER_ID,BOOKING_ID)
    cursor.execute(query),
    BOOKING = cursor.fetchall()
    cursor.close()
    return BOOKING
def get_location(FLIGHT_ID):
    db = get_db()
    cursor = db.cursor()

    query = """
    SELECT 
        o.IATA_CODE_PORT AS OriginAirportCode,
        o.LATITUDE AS OriginLatitude,
        o.LONGITUDE AS OriginLongitude,
        d.IATA_CODE_PORT AS DestinationAirportCode,
        d.LATITUDE AS DestinationLatitude,
        d.LONGITUDE AS DestinationLongitude
    FROM 
        ToAndFrom t
    JOIN 
        Airport o ON t.ORIGIN_AIRPORT = o.IATA_CODE_PORT
    JOIN 
        Airport d ON t.DESTINATION_AIRPORT = d.IATA_CODE_PORT
    WHERE 
        t.FLIGHT_ID = %s;
    """

    cursor.execute(query, (FLIGHT_ID,))
    location = cursor.fetchall()
    cursor.close()
    return location
