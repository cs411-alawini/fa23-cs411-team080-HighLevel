import React from 'react'
import './TopNavbar.css'
import AirlinesIcon from '@mui/icons-material/Airlines';

function TopNavbar() {
  return (
    <nav className='TopNavbar'>
        <a 
            className='Logo'
            onClick={() => {
                window.location.pathname = "/home"
            }}
        >
            <AirlinesIcon /> EasyBooking
        </a>
    </nav>
  )
}

export default TopNavbar
