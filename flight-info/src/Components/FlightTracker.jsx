import React, { useEffect, useState } from 'react';
import axios from 'axios';
import "./FlightTracker.css"
import { useLocation } from 'react-router-dom';

export const FlightTracker = () => {
    const location = useLocation();
    const flightId = location.state?.key;
    console.log(flightId);
    const [imageUrl, setImageUrl] = useState(null);

    useEffect(() => {
        if (!flightId) {
            console.error('No flight ID provided');
            return;
        }

        const fetchImage = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/map', {
                    params: { flightId },
                    responseType: 'blob',
                });

                const imageObjectURL = URL.createObjectURL(response.data);
                setImageUrl(imageObjectURL);
            } catch (error) {
                console.error('Error fetching image:', error);
            }
        };

        fetchImage();
    }, [flightId]); // Dependency on flightId

    return (
        <div className='Tracker1'>
            {imageUrl ? (
                <img 
                    src={imageUrl} 
                    alt="Flight Map" 
                    style={{ 
                        maxWidth: '100%', 
                        maxHeight: '100%', 
                        width: 'auto', 
                        height: 'auto' 
                    }}
                />
            ) : (
                <p>Loading image...</p>
            )}
        </div>
    );
};
