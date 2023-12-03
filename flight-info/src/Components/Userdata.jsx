import React, { useState, useEffect} from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

export const UserData = ({UID}) => {
    const [Udata, setdata] = useState([]);

    const handlefetchdata = async () => {
        try {
            console.log("handle get user data called")
            const response = await axios.get('http://127.0.0.1:5000/get_user', {
                params: {
                    userid:UID
                    // Add other parameters like YEAR, MONTH, DAY if needed
                }
            });
          
            console.log(response);
            // setSearchResults(response.data);
            setdata(response.data);
        } catch (err) {
          console.error('Error during fetch:', err);
        }
    };

    useEffect(() => {
        // Check if UID is not 0 or -1 before fetching data
        if (UID !== 0 && UID !== -1) {
            handlefetchdata();
        }
    }, [UID]);

    return (
        <div>
            {UID == 0 ? (
            <p>Waiting</p>
          ) : UID === -1 ? (
            <p>Not logged in yet.</p>
          ): (
            <>
            <ul>
           {Udata.map((result, index) => (
            <li key={index}>
              {/* Display relevant information from each result */}
              
              <p>UID: {result[0]}</p>
              <p>Pw: {result[1]}</p>
              <p>Points: {result[2]}</p>
              <p>Most Visited Airports: {result[3]}</p>
              <p>Most Visited time: {result[5]}</p>
              <p>Worst Airline: {result[4]}</p>
              <p>Average Delay: {result[6]}</p>
            </li>
          ))}
        </ul>
            </>
          )}
        </div>
       
    )
}

UserData.propTypes = {
    UID: PropTypes.number.isRequired,
  };