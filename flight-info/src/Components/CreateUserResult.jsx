import React from 'react';
import PropTypes from 'prop-types';

export const CreateUserResult = ({ CUResults }) => {
    return (
        <div>
            {CUResults == 200 ? (
            <p>Successed.</p>
          ) : CUResults === 0 ? (
            <p>Waiting.</p>
          ): (
            <p>Failed.</p>
          )}
        </div>
       
    )
}

CreateUserResult.propTypes = {
    CUResults: PropTypes.number.isRequired,
  };