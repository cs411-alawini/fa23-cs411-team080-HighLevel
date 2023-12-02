import React from 'react'
import "./Home.css"
import { SearchBar } from "./SearchBar";

function Home() {
  return (
    <div>
      <div className='Text'>
        <h2>
          Search your flight below!
        </h2>

        <SearchBar />
      </div>

    </div>
  )
}

export default Home