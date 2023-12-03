import React from 'react';
import PropTypes from 'prop-types';

export const LoginUserResult = ({ loggedResults }) => {
    return (
        <div>
            {loggedResults == 200 ? (
            <p>Successed.</p>
          ) : loggedResults === 0 ? (
            <p>Waiting.</p>
          ): (
            <p>Failed.</p>
          )}
        </div>
       
    )
}

LoginUserResult.propTypes = {
    loggedResults: PropTypes.number.isRequired,
  };