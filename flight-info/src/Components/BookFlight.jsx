// import React from 'react';
// import axios from 'axios'; // Don't forget to import axios

// export const BookFlight = ({ uid }) => {
//     const [flightId, setFlightId] = useState('');
// //   const [bookedFlights, setBookedFlights] = useState([]);

//     const handleFlightID = (e) => {
//         setFlightId(e.target.value);
//     };

//   const handleBook = async () => {
//     try {
//       console.log("handle book flight called");
//       const response = await axios.post('http://127.0.0.1:5000/add_booking', {
//         userid: uid,
//         flightId: flightId,
//       });

//       console.log(response.data);
//     } catch (err) {
//       console.error('Error during booking:', err);
//     }
//   };

//   const handleDelete = async (flightIdToDelete) => {
//     try {
//       console.log("handle delete flight called");
//       const response = await axios.delete('http://127.0.0.1:5000/delete_flight', {
//         data: {
//           userid: uid,
//           flightId: flightIdToDelete,
//         },
//       });

//       console.log(response.data);
//       // Handle the response data appropriately
//       // For example, update state or display a success message
//     } catch (err) {
//       console.error('Error during deleting flight:', err);
//       // Handle error scenarios
//     }
//   };

//   return (
//     <div>
//       <div>
//         <input
//             type="text"
//             placeholder="Search your flightID"
//             value={flightId}
//             onChange={handleFlightID}
//         />
//       </div>

//       <div className='BookFlightButton'>
//         <button onClick={handleBook}>
//         {/* <button> */}
//           Book This Flight
//         </button>
//       </div>

//       {/* Display booked flights and allow deletion */}
//       <div>
//         <h2>Booked Flights:</h2>
//         <ul>
//           {bookedFlights.map((flight) => (
//             <li key={flight.id}>
//               Flight ID: {flight.id} -{' '}
//               <button onClick={() => handleDelete(flight.id)}>
//                 Delete this booking
//               </button>
//             </li>
//           ))}
//         </ul>
//       </div>
//     </div>
//   );


//   return (
//     <div>
//       <div>
//         <input
//           type="text"
//           placeholder="Search your flightID"
//           value={flightId}
//           onChange={handleFlightID}
//         />
//       </div>

//       <div className='BookFlightButton'>
//         <button onClick={handleBook}>
//           Book This Flight
//         </button>
//       </div>

//       {/* Display booked flights and allow deletion */}
//       {/* Implement code to display booked flights and handle deletion */}
//     </div>
//   );
// };



import React, { useState, useEffect } from 'react';
import "./BookFlight.css"
import axios from 'axios'; // Don't forget to import axios
import PropTypes from 'prop-types';

export const BookFlight = ({ UID }) => {
  const [flightId, setFlightId] = useState('');
  const [bookedFlights, setBookedFlights] = useState([]);

  const handleFlightID = (e) => {
    setFlightId(e.target.value);
  };

  const handleBook = async () => {
    try {
      console.log("handle book flight called");
      console.log("UserID: ", UID);
      const response = await axios.post('http://127.0.0.1:5000/add_booking', {
        data: {
          userid: UID,
          flightId: flightId,
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
              <th>BookingID;</th>
              <th>FlightID;</th>
              <th>Book Date;</th>
            </tr>
          </thead>
          <tbody>
            {bookedFlights.map((result, index) => (
              <tr key={index}>
                <td>{result[0]}</td>
                <td>{result[2]}</td>
                <td>{result[3]}</td>
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
