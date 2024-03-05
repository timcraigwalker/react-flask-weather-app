import FavoriteIcon from '@mui/icons-material/Favorite';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import { Box, Card, CardContent, CardHeader, CardMedia, IconButton, Typography } from "@mui/material";

const CurrentWeather = ({weather, onFavouriteCitiesChange}) => {

    const addFavouriteCity = async () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                "city": weather.city,
                "latitude": weather.latitude,
                "longitude": weather.longitude
            }),
            credentials: "include"
        };
        try {
            const response = await fetch(`api/user/${weather.user_id}/favourite_cities`, requestOptions);
            const responseJson = await response.json();
            console.log(responseJson);
            // TODO: Show notification that favourite city was added
            onFavouriteCitiesChange();
        } catch (error) {
            console.error(error);
        }
    };

    const removeFavouriteCity = async () => {
        const requestOptions = {
            method: "DELETE",
            credentials: "include"
        };
        try {
            const response = await fetch(`api/user/${weather.user_id}/favourite_cities/${weather.favourite_id}`, requestOptions);
            const responseJson = await response.json();
            console.log(responseJson);
            // TODO: Show notification that favourite city was removed

            onFavouriteCitiesChange();
        } catch (error) {
            console.error(error);
        }
    };

    /*{ !weather.favourite_id && <Button size="small" onClick={addFavouriteCity}>Add to Favourites</Button> }
                        { weather.favourite_id && <Button size="small" onClick={removeFavouriteCity}>Remove from Favourites</Button> }*/

    return (
        <>
        {weather.current && (
            <Card
                variant="outlined"
            >
                <CardHeader
                    title={weather.city}
                    action={
                        !weather.favourite_id ? 
                            <IconButton aria-label="add to favorites" title="Add to favorites" onClick={addFavouriteCity}>
                                <FavoriteBorderIcon  />
                            </IconButton>
                        : 
                            <IconButton aria-label="remove from favorites" title="Remove from favorites" onClick={removeFavouriteCity}>
                                <FavoriteIcon />
                            </IconButton>
                    }
                />
                <Box sx={{ display: "flex", flexDirection: "row", justifyContent: "space-around" }}>
                    <CardMedia
                        component="img"
                        sx={{ maxWidth: 160, maxHeight: 160 }}
                        image={`weatherIcons/${weather.current.weather[0].icon}.png`}
                        alt="Weather"
                    />
                    <Box sx={{ display: "flex", flexDirection: "column" }}>
                        <CardContent>
                            <Typography component="div" variant="h3">
                                {Math.round(weather.current.temp)}°C
                            </Typography>
                            <Typography component="div" variant="subtitle1" color="text.secondary">
                                {weather.current.weather[0].description}
                            </Typography>
                            <Typography component="div" variant="string" color="text.secondary">
                                Feels like {Math.round(weather.current.feels_like)}°C
                            </Typography>
                        </CardContent>
                    </Box>
                </Box>
            </Card>
        )}
        </>
    )
}

export default CurrentWeather;