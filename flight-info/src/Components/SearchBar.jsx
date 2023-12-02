import React, { useState } from 'react';
import "./SearchBar.css"
import { FaSearch } from 'react-icons/fa';
import FlightTakeoffIcon from '@mui/icons-material/FlightTakeoff';
import FlightLandIcon from '@mui/icons-material/FlightLand';

export const SearchBar = () => {
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');

  const handleOriginChange = (e) => {
    setOrigin(e.target.value);
  };

  const handleDestinationChange = (e) => {
    setDestination(e.target.value);
  };

  const handleSearch = () => {
    // Perform search or other actions with origin and destination values
    console.log('Origin:', origin);
    console.log('Destination:', destination);
  };

  return (
    <div>
        <ul className='Search'>
            <div className='OrignationSearch'>
                <FlightTakeoffIcon />
                <input
                type="text"
                placeholder="Type Airport Code..."
                value={origin}
                onChange={handleOriginChange}
                />
            </div>

            <div className='DestinationSearch'>
                <FlightLandIcon />
                <input
                type="text"
                placeholder="Type Airport Code..."
                value={destination}
                onChange={handleDestinationChange}
                />
            </div>

            <div className='SearchButton'>
                <button onClick={handleSearch}>
                    <FaSearch />
                    Search
                </button>
            </div>
        </ul>
    </div>
  );
};
