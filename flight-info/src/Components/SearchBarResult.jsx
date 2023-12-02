import React from 'react';
import PropTypes from 'prop-types';

export const SearchBarResult = ({ searchResults }) => {
  return (
    <div className='SearchResults'>
      <h3>Search Results</h3>
      {searchResults.length === 0 ? (
        <p>No results found.</p>
      ) : (
        <ul>
          {searchResults.map((result, index) => (
            <li key={index}>
              {/* Display relevant information from each result */}
              
              <p>Flight ID: {result[0]}</p>
              <p>Departure Airport: {result[1]}</p>
              <p>Arrival Airport: {result[2]}</p>
              <p>Flight Number: {result[5]}</p>
              <p>Year: {result[6]}</p>
              <p>Arrival Airport: {result[7]}</p>
              <p>Arrival Airport: {result[8]}</p>
              <p>Arrival Airport: {result[9]}</p>
              <p>Arrival Airport: {result[10]}</p>
              <p>Arrival Airport: {result[11]}</p>
              <p>Arrival Airport: {result[12]}</p>
              <p>Arrival Airport: {result[13]}</p>
              <p>Arrival Airport: {result[14]}</p>
              <p>Arrival Airport: {result[15]}</p>
              <p>Arrival Airport: {result[16]}</p>
              <p>Arrival Airport: {result[17]}</p>
              <p>Arrival Airport: {result[18]}</p>
              <p>Arrival Airport: {result[19]}</p>
              {/* Add more details as needed */}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

SearchBarResult.propTypes = {
  searchResults: PropTypes.array.isRequired,
};