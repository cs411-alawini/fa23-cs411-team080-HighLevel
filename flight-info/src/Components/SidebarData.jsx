import React from 'react'
import HomeIcon from '@mui/icons-material/Home';
import BookmarkIcon from '@mui/icons-material/Bookmark';
import InfoIcon from '@mui/icons-material/Info';
import ConnectingAirportsIcon from '@mui/icons-material/ConnectingAirports';


export const SidebarData = [
    {
        title: "Home",
        icon: <HomeIcon />,
        link: "/home"
    },
    {
        title: "About",
        icon: <InfoIcon />,
        link: "/about"
    },
    {
        title: "Your Bookings",
        icon: <BookmarkIcon />,
        link: "/yourBookings"
    },
    {
        title: "Airports",
        icon: <ConnectingAirportsIcon />,
        link: "/airports"
    }
]