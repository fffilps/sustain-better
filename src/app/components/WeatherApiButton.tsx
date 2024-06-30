"use client"
import { useEffect, useState } from "react"


type Props = {}

const WeatherApiButton = (props: Props) => {
    const [pathDescriptions, setPathDescriptions] = useState("")

    const fetchData = async () => {
        
            const query = await fetch("https://api.weather.gov/openapi.json")
            const response = await query.json()
            console.log('Response from API ', response.components.responses.Observation.description)
            setPathDescriptions(response.components.responses.Observation.description)
          
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
              <div>{pathDescriptions}</div>
            )
          }
        </div>
      </main>
    );
}

export default WeatherApiButton