import React from 'react'
import "./Home.css"
import FlightTakeoffIcon from '@mui/icons-material/FlightTakeoff';
import FlightLandIcon from '@mui/icons-material/FlightLand';

function Home() {
  return (
    <div className='Text'>
      <h2>
        Search your flight below!
      </h2>

      <div>
        <ul className='Dropdown'>
          <div className='OriginationDropdown'>
            <p className='Origination'><FlightTakeoffIcon/> Origination</p>
            <select>
              <option>--Select Airport--</option>
            </select>
          </div>

          <div className='DestinationDropdown'>
            <p className='Destination'><FlightLandIcon/> Destination</p>
            <select>
              <option>--Select Airport--</option>
            </select>
          </div>
        </ul>
        
        

      </div>
    </div>
  )
}

export default Home
