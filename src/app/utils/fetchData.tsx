"use client";
import { useEffect, useState } from "react";

export default function Home() {
  const [pathDescriptions, setPathDescriptions] = useState("");

  useEffect(() => {
    const getData = async () => {
      const query = await fetch("https://api.weather.gov/alerts/active");
      const response = await query.json();
      console.log(
        "Response from API ",
        response
      );
      setPathDescriptions(
        response.components.responses.Observation.description,
      );
    };

    getData();
  }, []);

  return (
    <main>
      <div>
        <h1 className="text-6xl">Sustain Better</h1>
        {pathDescriptions && pathDescriptions.length && (
          <div>{pathDescriptions}</div>
        )}
      </div>
    </main>
  );
}
