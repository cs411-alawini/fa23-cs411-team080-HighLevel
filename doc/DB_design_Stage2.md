# ER diagram:
![Alt Text](https://github.com/cs411-alawini/fa23-cs411-team057-titans/blob/main/doc/ERdiag.png)


## Entities:

### User:
**Description:** This entity represents user login information.

**Attributes:**
- `USER_ID` (Primary Key, String): A unique identifier for users.
- `USERNAME` (String): The username for login.
- `PASSWORD` (String): The user's password (should be securely hashed).

**Assumptions:**
- Every user has a unique `USER_ID`.
- Users can change their password.
- Usernames are unique, ensuring that each user has a distinct login identity.

### Booking:
**Description:** This entity represents flight bookings made by users.

**Attributes:**
- `BOOKING_ID` (Primary Key, String): A unique identifier for each booking.
- `USER_ID` (Primary Key, Foreign Key to User.USER_ID): References the user who made the booking.
- `PRICE` (Integer): The price of the booking.
- `BOOKED_DATE` (Datetime): The date and time when the booking was made.

**Assumptions:**
- `BOOKING_ID` is unique for each booking.
- `USER_ID` references a valid user in the User entity.
- `PRICE` represents the total booking cost.
- `BOOKED_DATE` records the date and time of the booking.
- Users can make multiple bookings, each with a unique `BOOKING_ID`.

### Airline:
**Description:** This entity represents airlines.

**Attributes:**
- `AIRLINE_NAME` (Primary Key, String): The name of the airline.
- `IATA_CODE` (Integer): The International Air Transport Association (IATA) code for the airline.

**Assumptions:**
- `AIRLINE_NAME` uniquely identifies airlines.
- `IATA_CODE` represents the airline's International Air Transport Association code, which is unique among airlines.

### Airport:
**Description:** This entity represents airports.

**Attributes:**
- `AIRPORT_NAME` (Primary Key, String): The name of the airport.
- `IATA_CODE` (Integer): The IATA code for the airport.
- `CITY` (String): The city where the airport is located.
- `STATE` (String): The state where the airport is located.
- `COUNTRY` (String): The country where the airport is located.
- `LATITUDE` (String): The latitude coordinates of the airport.
- `LONGITUDE` (String): The longitude coordinates of the airport.

**Assumptions:**
- `AIRPORT_NAME` uniquely identifies airports.
- `IATA_CODE` represents the airport's International Air Transport Association code, which is unique among airports.
- Airports can be located in various cities, states, and countries.
- `LATITUDE` and `LONGITUDE` provide geographical coordinates for airports.

### Flight:
**Description:** This entity represents individual flights operated by airlines.

**Attributes:**
- `FLIGHT_ID` (Primary Key, String): A unique identifier for each flight.
- `FLIGHT_NUMBER` (Integer): The flight number assigned by the airline.
- `AIRLINE_IATA` (Foreign Key to Airline.IATA_CODE): References the airline operating the flight.
- `ORIGIN_AIRPORT` (Foreign Key to Airport.IATA_CODE): References the origin airport of the flight.
- `DESTINATION_AIRPORT` (Foreign Key to Airport.IATA_CODE): References the destination airport of the flight.
- `TAIL_NUMBER` (String): The tail number of the aircraft used for the flight.

**Assumptions:**
- `FLIGHT_ID` is unique for each flight.
- `FLIGHT_NUMBER` is unique within an airline.
- `AIRLINE_IATA` references a valid airline in the Airline entity.
- `ORIGIN_AIRPORT` and `DESTINATION_AIRPORT` reference valid airports in the Airport entity.
- `TAIL_NUMBER` represents the specific aircraft used for the flight, which may not be unique across flights.

### Trip:
**Description:** This entity represents information about trips taken by users, consisting of one or more flights.

**Attributes:**
- `FLIGHT_ID` (Foreign Key to Flight.FLIGHT_ID): References the flight(s) associated with the trip.
- `YEAR` (Integer): Year of the trip.
- `MONTH` (Integer): Month of the trip.
- `DAY` (Integer): Day of the trip.
- `DAY_OF_WEEK` (Integer): Day of the week of the trip.
- `SCHEDULED_DEPARTURE` (Integer): Scheduled departure time of the trip.
- `DEPARTURE_TIME` (Integer): Actual departure time of the trip.
- `DEPARTURE_DELAY` (Integer): Delay in departure.
- `TAXI_OUT` (Integer): Taxi out time.
- `WHEELS_OFF` (Integer): Time when the wheels leave the ground.
- `SCHEDULED_TIME` (Integer): Scheduled flight time.
- `ELAPSED_TIME` (Integer): Elapsed flight time.
- `AIR_TIME` (Integer): Time spent in the air.
- `DISTANCE` (Integer): Distance traveled.
- `WHEELS_ON` (Integer): Time when the wheels touch down.
- `TAXI_IN` (Integer): Taxi in time.
- `SCHEDULED_ARRIVAL` (Integer): Scheduled arrival time.
- `ARRIVAL_TIME` (Integer): Actual arrival time.
- `ARRIVAL_DELAY` (Integer): Delay in arrival.
- `DIVERTED` (Boolean): Whether the flight was diverted.
- `CANCELED` (Boolean): Whether the flight was canceled.
- `CANCELLATION_REASON` (String): Reason for flight cancellation.
- `AIR_SYSTEM_DELAY` (Boolean): Indicates if there was an air system delay.
- `SECURITY_DELAY` (Boolean): Indicates if there was a security delay.
- `AIRLINE_DELAY` (Boolean): Indicates if there was an airline delay.
- `LATE_AIRCRAFT_DELAY` (Boolean): Indicates if there was a late aircraft delay.
- `WEATHER_DELAY` (Boolean): Indicates if there was a weather delay.

**Assumptions:**
- `BOOKING_ID` references a valid booking in the Booking entity.
- `FLIGHT_ID` references valid flights in the Flight entity.
- `YEAR`, `MONTH`, `DAY`, and `DAY_OF_WEEK` define the date of the trip.
- Various attributes (e.g., `SCHEDULED_DEPARTURE`, `DEPARTURE_DELAY`) provide detailed flight information.
- Boolean fields (e.g., `DIVERTED`, `CANCELED`) indicate specific flight conditions.
- `CANCELLATION_REASON` records reasons for flight cancellations.
- Boolean fields (e.g., `AIR_SYSTEM_DELAY`, `SECURITY_DELAY`) flag various types of delays.
- Users can have multiple trips associated with different bookings and flights.

# Normalization:

## User:
- **Primary Key:** `USER_ID`
- **Functional Dependency:** `USERNAME` and `PASSWORD` are functionally dependent only on the `USER_ID`.
- **Direct Dependency:** All attributes are directly dependent on the primary key.
- **Normal Form:** This table is in BCNF.

## Booking:
- **Attributes:** `BOOKING_ID` is a unique attribute and `USER_ID` is a foreign key.
- **Direct Dependency:** `PRICE` and `BOOKED_DATE` are directly dependent on `BOOKING_ID`.
- **Normal Form:** This table is in BCNF.

## Airline:
- **Primary Key:** `AIRLINE_NAME`
- **Functional Dependency:** `IATA_CODE` is dependent on `AIRLINE_NAME`.
- **Normal Form:** This table is in BCNF.

## Airport:
- **Primary Key:** `AIRPORT_NAME`
- **Functional Dependency:** All other attributes are functionally dependent only on `AIRPORT_NAME`.
- **Normal Form:** This table is in BCNF.

## Flight:
- **Primary Key:** `FLIGHT_ID`
- **Direct Dependency:** All other attributes (including `FLIGHT_NUMBER`, `AIRLINE_IATA`, `ORIGIN_AIRPORT`, `DESTINATION_AIRPORT`, and `TAIL_NUMBER`) depend directly on the `FLIGHT_ID`.
- **Normal Form:** This table is in BCNF.

## Trip:
- **Composite Key:** Since there can be multiple trips associated with a booking and flight, a composite key (`BOOKING_ID`, `FLIGHT_ID`) might be the best choice.
- **Direct Dependency:** All other attributes depend on this composite key.
- **Normal Form:** This table is in BCNF.

# Relationships:

## Information:

**Entities Involved:** Airline and Flight  
**Cardinality:** One-to-Many (1:N) from Airline to Flight  
**Description:** One airline can operate multiple flights, but each flight is operated by only one airline.

**Assumptions:**  
- An airline can operate multiple flights, but each flight is operated by only one airline.
- Each flight is associated with exactly one airline.
- The relationship between an airline and a flight is based on the operational ownership of the flight.

## To and From:

**Entities Involved:** Flight and Airport  
**Cardinality:** Many-to-Many (N:M) from Flight to Airport  
**Description:** Each flight has multiple airports one for arrival and one for departure. And each airport holds multiple flights.

**Assumptions:**  
- Each flight has two airports associated with it - one for departure and one for arrival.
- Each airport can be associated with multiple flights for both departure and arrival.
- The relationship between a flight and an airport is based on the origin and destination of the flight.

## Books:

**Entities Involved:** User and Booking  
**Cardinality:** One-to-Many  
**Description:** A user can make multiple bookings, but each booking is made by only one user.

**Assumptions:**  
- A user can make multiple bookings, but each booking is made by only one user.
- Each booking is associated with exactly one user.
- The relationship between a user and a booking is based on the user's ownership of the booking.

## Operates:

**Entities Involved:** Flight and Trips  
**Cardinality:** One-to-Many  
**Description:** Each Trip has one flight, and one flight contains many trip information.

**Assumptions:**  
- Each trip is associated with exactly one flight, representing the specific journey taken by the user.
- One flight can be associated with multiple trips, as different users can take the same flight at different times.
- The relationship between a flight and a trip is based on the specific flight taken as part of a trip.

## Corresponding to:

**Entities Involved:** Trips and Booking  
**Cardinality:** One-to-Many  
**Description:** Each trip has multiple bookings, but one booking can only have one flight.

**Assumptions:**  
- Each trip can have multiple bookings associated with it, but one booking can only be associated with one flight (representing a specific journey).
- The relationship between a trip and a booking represents the different bookings associated with a single trip.
- The association between a trip and a booking is based on the fact that a user can book multiple trips, and each trip can have multiple bookings (e.g., for different passengers or services within the trip).


# Relational Schema:

## User:
```
User(
		USER_ID VARCHAR(255) [PK],
		USERNAME VARCHAR(255),
		PASSWORD VARCHAR(255)
)
```
## Booking:
```
Booking(
		BOOKING_ID VARCHAR(255) [PK],
		USER_ID VARCHAR(255) [PK] [FK to User.USER_ID],
		FLIGHT_ID [FK to Trip.FLIGHT_ID],
		PRICE INT,
		BOOKED_DATE DATETIME
)
```
## Airline:
```
Airline(
		AIRLINE_NAME VARCHAR(255) [PK],
		IATA_CODE INT
)
```
## Airport:
```
Airport(
		AIRPORT_NAME VARCHAR(255) [PK],
		IATA_CODE INT,
		CITY VARCHAR(255),
		STATE VARCHAR(255),
		COUNTRY VARCHAR(255),
		LATITUDE VARCHAR(255),
		LONGITUDE VARCHAR(255)
)
```
## Flight:
```
Flight(
		FLIGHT_ID VARCHAR(255) [PK],
		FLIGHT_NUMBER INT,
		AIRLINE_IATA INT [FK to Airline.IATA_CODE],
		ORIGIN_AIRPORT VARCHAR(255),
		DESTINATION_AIRPORT VARCHAR(255),
		TAIL_NUMBER VARCHAR(255)
)
```
## Trip:
```
Trip(
		FLIGHT_ID VARCHAR(255) [FK to Flight.FLIGHT_ID],
		YEAR INT,
		MONTH INT,
		DAY INT,
		DAY_OF_WEEK INT,
		SCHEDULED_DEPARTURE INT,
		DEPARTURE_TIME INT,
		DEPARTURE_DELAY INT,
		TAXI_OUT INT,
		WHEELS_OFF INT,
		SCHEDULED_TIME INT,
		ELAPSED_TIME INT,
		AIR_TIME INT,
		DISTANCE INT,
		WHEELS_ON INT,
		TAXI_IN INT,
		SCHEDULED_ARRIVAL INT,
		ARRIVAL_TIME INT,
		ARRIVAL_DELAY INT,
		DIVERTED BOOL,
		CANCELED BOOL,
		CANCELLATION_REASON VARCHAR(255),
		AIR_SYSTEM_DELAY BOOL,
		SECURITY_DELAY BOOL,
		AIRLINE_DELAY BOOL,
		LATE_AIRCRAFT_DELAY BOOL,
		WEATHER_DELAY BOOL
)
```
## ToAndFrom:
```
ToAndFrom(
		FLIGHT_ID VARCHAR(255) [FK to Flight.FLIGHT_ID],
		ORIGIN_AIRPORT VARCHAR(255) [FK to Airport.IATA_CODE],
		DESTINATION_AIRPORT VARCHAR(255) [FK to Airport.IATA_CODE],
		PRIMARY KEY (FLIGHT_ID, ORIGIN_AIRPORT, DESTINATION_AIRPORT),
		FOREIGN KEY (FLIGHT_ID) REFERENCES Flight.FLIGHT_ID ON DELETE CASCADE,
		FOREIGN KEY (ORIGIN_AIRPORT) REFERENCES Airport.IATA_CODE ON DELETE CASCADE,
		FOREIGN KEY (DESTINATION_AIRPORT) REFERENCES Airport.IATA_CODE ON DELETE CASCADE
)
)
```
# DDL Commands in MySQL

```sql
CREATE TABLE User (
    USER_ID VARCHAR(255) PRIMARY KEY,
    USERNAME VARCHAR(255),
    PASSWORD VARCHAR(255)
);

CREATE TABLE Booking (
    BOOKING_ID VARCHAR(255),
    USER_ID VARCHAR(255) NOT NULL,
    PRICE INT,
    FLIGHT_ID VARCHAR(255),
    BOOKED_DATE DATETIME,
    PRIMARY KEY(USER_ID, BOOKING_ID),
    FOREIGN KEY (USER_ID) REFERENCES User.USER_ID ON DELETE CASCADE
    FOREIGN KEY (FLIGHT_ID) REFERENCES Trip.FLIGHT_ID ON DELETE CASCADE
);

CREATE TABLE Airline (
    AIRLINE_NAME VARCHAR(255) PRIMARY KEY,
    IATA_CODE INT
);

CREATE TABLE Airport (
    AIRPORT_NAME VARCHAR(255) PRIMARY KEY,
    IATA_CODE INT,
    CITY VARCHAR(255),
    STATE VARCHAR(255),
    COUNTRY VARCHAR(255),
    LATITUDE VARCHAR(255),
    LONGITUDE VARCHAR(255)
);

CREATE TABLE Flight (
    FLIGHT_ID VARCHAR(255) PRIMARY KEY,
    FLIGHT_NUMBER INT,
    AIRLINE_IATA INT,
    ORIGIN_AIRPORT VARCHAR(255),
    DESTINATION_AIRPORT VARCHAR(255),
    TAIL_NUMBER VARCHAR(255),
    FOREIGN KEY (AIRLINE_IATA) REFERENCES Airline.IATA_CODE ON DELETE CASCADE
);

CREATE TABLE Trip (
    FLIGHT_ID VARCHAR(255),
    YEAR INT,
    MONTH INT,
    DAY INT,
    DAY_OF_WEEK INT,
    SCHEDULED_DEPARTURE INT,
    DEPARTURE_TIME INT,
    DEPARTURE_DELAY INT,
    TAXI_OUT INT,
    WHEELS_OFF INT,
    SCHEDULED_TIME INT,
    ELAPSED_TIME INT,
    AIR_TIME INT,
    DISTANCE INT,
    WHEELS_ON INT,
    TAXI_IN INT,
    SCEHDULED_ARRIVAL INT,
    ARRIVAL_TIME INT,
    ARRIVAL_DELAY INT,
    DIVERTED BOOL,
    CANCELED BOOL,
    CANCELLATION_REASON VARCHAR(255),
    AIR_SYSTEM_DELAY BOOL,
    SECURITY_DELAY BOOL,
    AIRLINE_DELAY BOOL,
    LATE_AIRCRAFT_DELAY BOOL,
    WEATHER_DELAY BOOL,
    FOREIGN KEY (FLIGHT_ID) REFERENCES Flight.FLIGHT_ID ON DELETE CASCADE
);

CREATE TABLE ToAndFrom (
    FLIGHT_ID VARCHAR(255),
    ORIGIN_AIRPORT VARCHAR(255),
    DESTINATION_AIRPORT VARCHAR(255),
    PRIMARY KEY (FLIGHT_ID, ORIGIN_AIRPORT, DESTINATION_AIRPORT),
    FOREIGN KEY (FLIGHT_ID) REFERENCES Flight.FLIGHT_ID ON DELETE CASCADE,
    FOREIGN KEY (ORIGIN_AIRPORT) REFERENCES Airport.IATA_CODE ON DELETE CASCADE,
    FOREIGN KEY (DESTINATION_AIRPORT) REFERENCES Airport.IATA_CODE ON DELETE CASCADE
);
```
