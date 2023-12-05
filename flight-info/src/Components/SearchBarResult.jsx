import React from 'react';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router-dom';

export const SearchBarResult = ({ searchResults }) => {
  const navigate = useNavigate();

  const handleNavigate = (flightID) => {
    navigate('/flightTracker', { state: { key: flightID } });
  };

  return (
    <div className='SearchResults'>
      <h3>Search Results</h3>
      {searchResults.length === 0 ? (
        <p>No results found.</p >
      ) : (
        <table>
          <thead>
            <tr>
              <th>Flight ID;</th>
              <th>Departure Airport;</th>
              <th>Arrival Airport;</th>
              <th>Flight Number;</th>
              <th>Tail Number;</th>
              <th>Year;</th>
              <th>Month;</th>
              <th>Day;</th>
              <th>Day Of Week;</th>
              <th>Arrival Ddelay;</th>
              <th>Flight Tracker</th>
            </tr>
          </thead>
          <tbody>
            {searchResults.map((result, index) => (
              <tr key={index}>
                <td>{result[0]}</td>
                <td>{result[1]}</td>
                <td>{result[2]}</td>
                <td>{result[5]}</td>
                <td>{result[33]}</td>
                <td>{result[6]}</td>
                <td>{result[7]}</td>
                <td>{result[8]}</td>
                <td>{result[9]}</td>
                <td>{result[23]}</td>
                <td>
                  <button onClick={() => handleNavigate(result[0])}>
                    Go to Flight Tracker
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

SearchBarResult.propTypes = {
  searchResults: PropTypes.array.isRequired,
};