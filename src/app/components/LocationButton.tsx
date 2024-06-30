"use client";
import React, { useState } from "react";

type Props = {
  // profile: {}
};

const LocationButton = (props: Props) => {
  const [longitude, setLongitude] = useState(Number);
  const [latitude, setLatitude] = useState(Number);

  const getLocation = () => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        setLatitude(position.coords.latitude);
        setLongitude(position.coords.longitude);
      },
      (error) => {
        console.log(error);
        switch (error.code) {
          case error.PERMISSION_DENIED:
            console.log("User denied the request for Geolocation");
            break;
          case error.POSITION_UNAVAILABLE:
            console.log("Location information is unavailable");
            break;
          case error.TIMEOUT:
            console.log("The request to get user location timed out.");
            break;
          default:
            console.log("An unknown error occurred.");
            break;
        }
      },
    );
  };

  return (
    <div className="flex flex-col gap-3 py-2">
      <button
        className="bg-green-300 text-black rounded-full py-2 px-4"
        onClick={getLocation}
      >
        Get Location
      </button>
      <p>Longitude: {longitude}</p>
      <p>Latitude: {latitude}</p>
    </div>
  );
};

export default LocationButton;
