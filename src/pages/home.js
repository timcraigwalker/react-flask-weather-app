import React, { useState } from "react";

import Search from "../components/Search/search";
import { Container, CssBaseline } from "@mui/material";
import Weather from "../components/Weather/weather";

const Home = () => {
    const [currentWeather, setCurrentWeather] = useState(null);
    const [forecast, setForecast] = useState(null);

    const handleOnSearchChange = (searchData) => {
        const [latitude, longitude] = searchData.value.split(" ");

        const currentWeatherFetch = fetch(`api/weather/current/${latitude}/${longitude}`);
        const forecastFetch = fetch(`api/weather/forecast/${latitude}/${longitude}`);

        Promise.all([currentWeatherFetch, forecastFetch])
        .then(async (response) => {
            const weatherResponse = await response[0].json();
            const forcastResponse = await response[1].json();

            if(response[0].status === 200 && response[1].status === 200)
            {
              setCurrentWeather({ city: searchData.label, ...weatherResponse });
              setForecast({ city: searchData.label, ...forcastResponse });
            }
        })
        .catch((error) => console.error(error));
    };
  

    return (
      <>
        <Container component="main" maxWidth="xl">
          <CssBaseline />
          <Search onSearchChange={handleOnSearchChange}/>
          {currentWeather && forecast && <Weather {...{currentWeather, forecast}} />}
        </Container>
      </>
    );
  }
  
  export default Home;