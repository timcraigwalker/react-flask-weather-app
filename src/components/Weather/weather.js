import { Box } from "@mui/material";
import { useEffect, useState } from "react";
import CurrentWeather from "./CurrentWeather/currentWeather";
import WeatherForecast from "./WeatherForecast/weatherForecast";

const Weather = ({user, city, latitude, longitude, id}) => {
    const [weather, setWeather] = useState(null);

    useEffect(() => {
        fetch(`api/weather/${latitude}/${longitude}`)
        .then(async (response) => {
            const weatherResponse = await response.json();

            if(response.status === 200)
            {
              setWeather({
                city: city,
                latitude: latitude,
                longitude: longitude,
                favourite_id: id,
                user_id: user,
                current: weatherResponse["current"],
                forecast: weatherResponse["daily"]
              });
            }
        })
        .catch((error) => console.error(error));
    }, [user, city, latitude, longitude, id]);

    return (
        <Box marginTop={1} width="360px">
            { weather && weather.current  && <CurrentWeather weather={weather} />}
            { weather && weather.forecast && <WeatherForecast weather={weather} />}
        </Box>
    )
}

export default Weather;