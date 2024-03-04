import { Card } from "@mui/material";
import { useEffect, useState } from "react";

const WeatherForecast = ({forecast}) => {

    const [formattedForecast, setformattedForecast] = useState([]);

    const getDayName = (value, locale) => {
        return new Date(value).toLocaleDateString(locale, {
            weekday: 'long'
        });
    };

    useEffect(() => {
        const formattedForecast = [];
    
        forecast.list.splice(0, 7).forEach((item) => {
            formattedForecast.push({
                "day": getDayName(item.dt * 1000, 'en-GB'),
                "max_temp": Math.round(item.main.temp_max),
                "min_temp": Math.round(item.main.temp_min),
                "description": item.weather[0].description,
                "image": `${item.weather[0].icon}.png`,
                "feels_like": `${item.main.feels_like}`
            });
        });
    
        setformattedForecast(formattedForecast);
    }, []);

    return (
        <>
            <Card>
                {formattedForecast.map((dayForecast) => (
                    <p>{dayForecast["day"]} {dayForecast["description"]} {dayForecast["max_temp"]} {dayForecast["min_temp"]}</p>
                ))}
            </Card>
        </>
    )
}

export default WeatherForecast;