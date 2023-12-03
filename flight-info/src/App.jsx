import { useState } from 'react'
import './App.css'
import Sidebar from './Components/Sidebar'
import TopNavbar from './Components/TopNavbar'
import Home from './Components/Home'
import About from './Components/About'
import Myflight from './Components/Myflight'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div className='App'>
      <Router>
        
        <TopNavbar />
        <Sidebar />
        <Routes>
            <Route exact path='/home' element={<Home />} />
            <Route path='/about' element={<About/>} />
            <Route caseSensitive={false} path='/myFlights' element={<Myflight/>} />
        </Routes>

        {/* <Sidebar /> */}
      </Router>
    </div>
    
  )
}

export default App
