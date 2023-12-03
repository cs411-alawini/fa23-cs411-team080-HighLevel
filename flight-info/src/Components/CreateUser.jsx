import React, { useState } from 'react';
import axios from 'axios';
import "./CreateUser.css"
import PropTypes from 'prop-types';

export const CreateUser = ({ updateCUResults }) => {
    const [uid, setUID] = useState('');
    const [pw, setPW] = useState('');
    const [error, setError] = useState('');
  
  
    const handleUIDChange = (e) => {
        setUID(e.target.value);
    };
  
    const handlePWChange = (e) => {
        setPW(e.target.value);
    };
  
  
  const handleCreate = async () => {
      setError('');
  
      try {
        console.log("handle createuser called")
        updateCUResults(1);
        // console.log(uid,pw)
        const response = await axios.post('http://127.0.0.1:5000/add_user', {
            userid: uid,
            password: pw,
            // Add other parameters like YEAR, MONTH, DAY if needed
        });
        console.log(response.status);
        // setSearchResults(response.data);
        // zzh:
        updateCUResults(response.status);
      } catch (err) {
        setError('Failed to create user. Please try again later.');
        console.error('Error during create user:', err);
      }
    };
  
  
    return (
      <div>
          <ul className='Search'>
              <div className='OrignationSearch'>
                  <input
                  type="text"
                  placeholder="Type USERID"
                  value={uid}
                  onChange={handleUIDChange}
                  />
              </div>
  
              <div className='DestinationSearch'>
                  <input
                  type="text"
                  placeholder="Type PASSWORD"
                  value={pw}
                  onChange={handlePWChange}
                  />
              </div>
  
              <div className='SearchButton'>
                  <button onClick={handleCreate}>
                      CREATE
                  </button>
              </div>
          </ul>
      </div>
    );
  };
  
  CreateUser.propTypes = {
    updateCUResults: PropTypes.func.isRequired,
  };