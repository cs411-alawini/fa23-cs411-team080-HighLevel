import React, { useState } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

export const LoginUser = ({ updateUIDLOGResults }) => {
    const [uid, setUID] = useState('');
    const [pw, setPW] = useState('');
    const [pwnew, setnewPW] = useState('');
    const [error, setError] = useState('');
  
  
    const handleUIDChange = (e) => {
        setUID(e.target.value);
    };
  
    const handlePWChange = (e) => {
        setPW(e.target.value);
    };

    const handlePWnewChange = (e) => {
        setnewPW(e.target.value);
    };
  
  
  const handleLogin = async () => {
      setError('');
  
      try {
        console.log("handle uselogin called")
        updateUIDLOGResults(1,-1)
        // console.log(uid,pw)
        const response = await axios.get('http://127.0.0.1:5000/login', {
            params: {
                userid: uid,
                password: pw,
            // Add other parameters like YEAR, MONTH, DAY if needed
            }
        });
        console.log(response.status);
        // setSearchResults(response.data);
        // zzh:
        updateUIDLOGResults(response.status,uid);
      } catch (err) {
        setError('Failed to create user. Please try again later.');
        console.error('Error during create user:', err);
      }
    };

    const handleChangePw = async () => {
      setError('');
  
      try {
        console.log("handle changepw called")
        updateUIDLOGResults(1,-1)
        // console.log(uid,pw)
        const response = await axios.get('http://127.0.0.1:5000/update_user', {
            params: {
                userid: uid,
                password: pw,
                newpassword: pwnew,
            // Add other parameters like YEAR, MONTH, DAY if needed
            }
        });
        console.log(response.status);
        // setSearchResults(response.data);
        // zzh:
        updateUIDLOGResults(response.status,uid);
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
                  <button onClick={handleLogin}>
                      LogIn
                  </button>
              </div>
              <div className='SearchButton'>
                  <button onClick={handleChangePw}>
                      ChangePassword
                  </button>
              </div>
          </ul>
      </div>
    );
  };
  
  LoginUser.propTypes = {
    updateUIDLOGResults: PropTypes.func.isRequired,
  };