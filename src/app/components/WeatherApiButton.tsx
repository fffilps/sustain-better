"use client"
import { useEffect, useState } from "react"


type Props = {}

const WeatherApiButton = (props: Props) => {
    const [pathDescriptions, setPathDescriptions] = useState([""])

    const fetchData = async () => {
        
            const query = await fetch("https://api.weather.gov/alerts/active")
            const response = await query.json()
            console.log(response)
            for(let x = 0; x < 10; x++) {
                setPathDescriptions((pathDescription) => [...pathDescription, response.features[x].properties.headline])
                console.log(response.features[x].properties.headline)
            }
            // const response = await query.json()
            // console.log('Response from API ', response.components.responses.Observation.description)
            // setPathDescriptions(response.components.responses.Observation.description)
          
    }
    // Will be used when loading data at beginning and then constant updating.
    // useEffect(() => {
    //   const getData = async () => {
    //     const query = await fetch("https://api.weather.gov/openapi.json")
    //     const response = await query.json()
    //     console.log('Response from API ', response.components.responses.Observation.description)
    //     setPathDescriptions(response.components.responses.Observation.description)
    //   }
  
    // }, [])
    
  
    return (
      <main className="py-2">
        <div>
            <button className="bordered rounded-lg bg-gray-500 p-4" onClick={fetchData}>API Call</button>
          {
            pathDescriptions && pathDescriptions.length && (
              <div className="flex flex-col gap-2 divide-y-4 py-2 justify-center items-center">{pathDescriptions.map((description, index) => (
                <div className=" text-center py-2" key={index}>
                    <div className="text-center">{description}</div>
                </div>
              ))}</div>
            )
          }
        </div>
      </main>
    );
}

export default WeatherApiButton