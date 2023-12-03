// import React from 'react';
// import PropTypes from 'prop-types';

// export const SearchBarResult = ({ searchResults }) => {
//   return (
//     <div className='SearchResults'>
//       <h3>Search Results</h3>
//       {searchResults.length === 0 ? (
//         <p>No results found.</p>
//       ) : (
//         <ul>
//           {searchResults.map((result, index) => (
//             <li key={index}>
//               {/* Display relevant information from each result */}
              
//               <p>Flight ID: {result[0]}</p>
//               <p>Departure Airport: {result[1]}</p>
//               <p>Arrival Airport: {result[2]}</p>
//               <p>Flight Number: {result[5]}</p>
//               <p>Tail Number: {result[33]}</p>
//               <p>Year: {result[6]}</p>
//               <p>Month: {result[7]}</p>
//               <p>Day: {result[8]}</p>
//               <p>Day Of Week: {result[9]}</p>
//               <p>Schedule Departure: {result[10]}</p>
//               <p>Departure Time: {result[11]}</p>
//               <p>Departure Delay: {result[12]}</p>
//               <p>Taxi Out: {result[13]}</p>
//               <p>Wheels Off: {result[14]}</p>
//               <p>Schedule Time: {result[15]}</p>
//               <p>Elapsed Time: {result[16]}</p>
//               <p>Air Time: {result[17]}</p>
//               <p>Distance(km): {result[18]}</p>
//               <p>Wheels On: {result[19]}</p>
//               <p>Taxi in: {result[20]}</p>
//               <p>Schedule Arrival: {result[21]}</p>
//               <p>Arrival Time: {result[22]}</p>
//               <p>Arrival Ddelay: {result[23]}</p>
//               <p>Diverted: {result[24]}</p>
//               <p>Cancelled: {result[25]}</p>
//               <p>Air System Delay: {result[27]}</p>
//               <p>Security Delay: {result[28]}</p>
//               <p>Airline Delay: {result[29]}</p>
//               <p>Late Aircraft Delay: {result[30]}</p>
//               <p>Weather Delay: {result[31]}</p>
//               {/* Add more details as needed */}
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// };

// SearchBarResult.propTypes = {
//   searchResults: PropTypes.array.isRequired,
// };


////
import React from 'react';
import PropTypes from 'prop-types';

export const SearchBarResult = ({ searchResults }) => {
  return (
    <div className='SearchResults'>
      <h3>Search Results</h3>
      {searchResults.length === 0 ? (
        <p>No results found.</p>
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
                {/* Add more cells as needed */}
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