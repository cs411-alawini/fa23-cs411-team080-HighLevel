import React, { useState } from 'react'
import "./Myflight.css"

// CREATE USER
import { CreateUser } from "./CreateUser";
import { CreateUserResult } from "./CreateUserResult";

// LOGIN/CHANGE PWD/DELETE
import { LoginUser } from "./LoginUser";
import { LoginUserResult } from "./LoginUserResult";

// UserData
import { UserData } from "./Userdata";

// BookFlight
import { BookFlight } from "./BookFlight";



function Myflight() {
    const [CUResults, setupdateCUResults] = useState(0);
    const [loggedResults, setLoggedUIDResults] = useState(0);
    const [UID, setLoggedUID] = useState("");

    const updateCUResults = (results) => {
        setupdateCUResults(results);
        console.log("Curesult changed")
        console.log(CUResults);
    };
    

    const updateUIDLOGResults = (results,uid) => {
        setLoggedUIDResults(results)
        setLoggedUID(uid);
        console.log("logged uid changed");
        console.log(loggedResults);
        console.log(UID);
    };

    return (
      <div className='Myflightlayer1'>
        <div>
            <h2>
            Create User
            </h2>
            <CreateUser updateCUResults={updateCUResults}/>
            <CreateUserResult CUResults={CUResults}/>
        </div>
        <div>
            <h2>
            User Login
            </h2>
            <LoginUser updateUIDLOGResults={updateUIDLOGResults}/>
            <LoginUserResult loggedResults={loggedResults}/>
        </div>
        <div>
            <h2>
            User Data
            </h2>
            <UserData UID = {UID}/>
        </div>

        <div>
            <h2>
                Book your flight here!
            </h2>
            <BookFlight UID = {UID} />
        </div>
        
      </div>
    )
  }
  
  export default Myflight