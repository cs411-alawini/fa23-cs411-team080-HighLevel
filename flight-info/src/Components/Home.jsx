import React, { useState } from 'react'
import "./Home.css"
import { SearchBar } from "./SearchBar";
import { SearchBarResult } from "./SearchBarResult";

function Home() {
  const [searchResults, setSearchResults] = useState([]);

  const updateSearchResults = (results) => {
    setSearchResults(results);
  };


  return (
    <div>
      <div className='Text'>
        <h2>
          Search your flight below!
        </h2>

        <SearchBar updateSearchResults={updateSearchResults}/>
        <SearchBarResult searchResults={searchResults}/>
      </div>
      

    </div>
  )
}

export default Home