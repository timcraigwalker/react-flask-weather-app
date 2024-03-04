import { Card, CardContent, Typography, Box, CardMedia } from "@mui/material";
import "./currentWeather.css"

const CurrentWeather = ({currentWeather}) => {
    console.log(currentWeather);
        /* City, Temperature, Weather, Feels Like (Possible Icon) */
    return (
        <>
        {currentWeather && (
            <Card
                variant="outlined"
                orientation="horizontal"
            >
                <Box sx={{ display: 'flex', flexDirection: 'row' }}>
                    <CardMedia
                        component="img"
                        sx={{ maxWidth: 120 }}
                        image={`weatherIcons/${currentWeather.weather[0].icon}.png`}
                        alt="Weather"
                    />
                    <CardContent>
                        <Typography component="div" variant="h5">
                            {currentWeather.city}
                        </Typography>
                        <Typography component="div" variant="subtitle1" color="text.secondary">
                            {currentWeather.weather[0].description}
                        </Typography>
                        <Typography component="div" variant="h3">
                            {Math.round(currentWeather.main.temp)}°C
                        </Typography>
                    </CardContent>
                </Box>
                <CardContent>
                    <Typography component="div" variant="h6">
                        Feels like {Math.round(currentWeather.main.feels_like)}°C
                    </Typography>
                </CardContent>
            </Card>
        )}
        </>
    )
}

export default CurrentWeather;