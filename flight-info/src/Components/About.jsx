import React from 'react'
import './About.css'
import ScreenSearchDesktopIcon from '@mui/icons-material/ScreenSearchDesktop';
import StorageIcon from '@mui/icons-material/Storage';

function About() {
  return (
    <div className='AboutText'>
      <h1>
        This is an easy flight searching and booking website.
      </h1>

      <h2>
        Developers:
      </h2>

      <div>
        <p><ScreenSearchDesktopIcon/> Frontend</p>
        <p>Jincheng Xu</p>
        <p>Zihao Zheng</p>
      </div>

      <div>
        <div><StorageIcon/> Backend</div>
        <p>Xinyu Chen</p>
        <p></p>
      </div>

    </div>
  )
}

export default About
