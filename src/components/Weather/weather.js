import { Box, Grid, Paper } from "@mui/material";
import { styled } from '@mui/material/styles';
import CurrentWeather from "./CurrentWeather/currentWeather";
import WeatherForecast from "./WeatherForecast/weatherForecast";

const Weather = ({currentWeather, forecast}) => {
    const Item = styled(Paper)(({ theme }) => ({}));
    

    return (
        <Box sx={{ flexGrow: 1 }} marginTop={1}>
            <Grid container>
                <Grid xs={12} sm={12}>
                <Item>{currentWeather  && <CurrentWeather currentWeather={currentWeather} />}</Item>
              </Grid>
              <Grid xs={12} sm={4}>
                <Item>{currentWeather  && <CurrentWeather currentWeather={currentWeather} />}</Item>
              </Grid>
              <Grid xs={12} sm={8}>
                <Item>{ forecast && <WeatherForecast forecast={forecast} />}</Item>
              </Grid>
            </Grid>
        </Box>
    )
}

export default Weather;