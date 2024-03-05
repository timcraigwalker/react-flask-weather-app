import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import { Accordion, AccordionDetails, AccordionSummary, Avatar, List, ListItem, ListItemAvatar, ListItemText, Typography } from "@mui/material";

const WeatherForecast = ({weather}) => {
    const getDayName = (value, locale) => {
        return new Date(value).toLocaleDateString(locale, {
            weekday: 'long'
        });
    };

    return (
        <>
            <Accordion disableGutters>
                <AccordionSummary
                    expandIcon={<ArrowDropDownIcon />}
                    aria-controls="forecast-content"
                    id="forecast-header"
                >
                    <Typography>8 Day Forecast</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <List dense sx={{ width: "100%", bgcolor: "background.paper" }} >
                        {weather.forecast.map((day, key) => (
                            <ListItem key={key}>
                                <ListItemAvatar>
                                    <Avatar alt="Weather" src={`weatherIcons/${day.weather[0].icon}.png`}></Avatar>
                                </ListItemAvatar>
                                <ListItemText
                                    primary={
                                        `${getDayName(day.dt * 1000, 'en-GB')} (${day.temp.min}°C / ${day.temp.max}°C)`
                                    }
                                    secondary={day.summary}
                                ></ListItemText>
                            </ListItem>
                        ))}
                    </List>
                </AccordionDetails>
            </Accordion>
        </>
    )
}

export default WeatherForecast;