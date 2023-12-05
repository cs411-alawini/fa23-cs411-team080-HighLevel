import React, { useState, useEffect } from 'react';
import "./BookFlight.css"
import axios from 'axios'; // Don't forget to import axios
import PropTypes from 'prop-types';

export const BookFlight = ({ UID }) => {
  const [flightId, setFlightId] = useState('');
  const [numberTicket, setNumberTicket] = useState('');
  const [bookedFlights, setBookedFlights] = useState([]);

  const handleFlightID = (e) => {
    setFlightId(e.target.value);
  };

  const handleNumber = (e) => {
    setNumberTicket(e.target.value);
  };

  const handleBook = async () => {
    try {
      console.log("handle book flight called");
      console.log("UserID: ", UID);
      const response = await axios.post('http://127.0.0.1:5000/add_booking', {
        data: {
          userid: UID,
          flightId: flightId,
          bookednumber: numberTicket,
        }
        
      });

      console.log(response.data);
      // Handle booking success or update UI accordingly
    } catch (err) {
      console.error('Error during booking:', err);
      // Handle booking error scenarios
    }
  };

  const handleDisplayBooked = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/get_booking', {
        params: {
          user_id: UID,
        }
       
      });
      // bookedFlights = response.data;
      setBookedFlights(response.data);
      console.log("handle Display called")
    } catch (err) {
      console.error('Error during fetch booked:', err);
    }
  };


  const handleDelete = async (bookingID) => {
    try {
      // Make a request to delete the booking with the given bookingID

      const response = await axios.delete('http://127.0.0.1:5000/delete_booking', {
        params: {
          user_id: UID,
          booking_id: bookingID,
        }
      });
      // Update the state or perform any necessary UI update after deletion
      console.log("handle Delete called")
      // For example, if you want to update the displayed booked flights after deletion:
      handleDisplayBooked();
    } catch (err) {
      console.error('Error during deletion:', err);
      // Handle deletion error scenarios
    }
  };

  
  const handleChange = async (bookingID) => {
    try {
      const response = await axios.put('http://127.0.0.1:5000/update_booking', {
        // params: {
          user_id: UID,
          bookingid: bookingID,
          flightid: flightId,
          bookednumber: numberTicket,
        // }
      });
      // Handle booking success or update UI accordingly
    } catch (err) {
      console.error('Error during booking:', err);
      // Handle booking error scenarios
    }
  };
  

  useEffect(() => {
    // Check if UID is not 0 or -1 before fetching data
    if (UID !== 0 && UID !== -1) {
      handleDisplayBooked();
    }
  }, [UID]);

  return (
    <div>
      <div>
        <input
          type="text"
          placeholder="Search your flightID"
          value={flightId}
          onChange={handleFlightID}
        />
      </div>

      <div>
        <input
          type="text"
          placeholder="Number of tickets"
          value={numberTicket}
          onChange={handleNumber}
        />
      </div>

      <div className='BookFlightButton'>
        <button onClick={handleBook}>
          Book This Flight
        </button>
      </div>

      {/* Display booked flights and allow deletion */}
      <div className='BookedList'>
        <h2>Booked Flights:</h2>
        <table>
          <thead>
            <tr>
              <th>BookingID </th>
              <th>FlightID </th>
              <th>Book Date </th>
              <th>Number Booked</th>
              <th>Delete this booking</th>
              <th>Change Amount </th>
            </tr>
          </thead>
          <tbody>
            {bookedFlights.map((result, index) => (
              <tr key={index}>
                <td>{result[0]}</td>
                <td>{result[2]}</td>
                <td>{result[3]}</td>
                <th>{result[4]}</th>
                <td>
                  <button onClick={() => handleDelete(result[0])}>
                    Delete booking
                  </button>
                </td>

                <td>
                  <div>
                    <input
                      type="text"
                      placeholder="Ticket number"
                      value={numberTicket}
                      onChange={handleNumber}
                    />
                  </div>

                  <button onClick={() => handleChange(result[0])}>
                    Change
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

BookFlight.propTypes = {
  UID: PropTypes.number.isRequired,
};
