import React, { useState } from 'react'
import "./Myflight.css"
import { CreateUser } from "./CreateUser";
import { CreateUserResult } from "./CreateUserResult";



function Myflight() {
    const [CUResults, setupdateCUResults] = useState(0);

    const updateCUResults = (results) => {
        setupdateCUResults(results);
        console.log("Curesult changed")
        console.log(CUResults);
    };

    return (
      <div className='Myflightlayer1'>
        <h2>
          Create User Below
        </h2>
        <CreateUser updateCUResults={updateCUResults}/>
        <CreateUserResult CUResults={CUResults}/>
      </div>
    )
  }
  
  export default Myflight