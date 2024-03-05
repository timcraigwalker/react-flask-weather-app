import { Box, Container, Divider, Typography } from "@mui/material";
import Weather from "../Weather/weather";

const FavouriteCities = ({favouriteCities, onFavouriteCitiesChange}) => {

    return (
        <>
            <Box marginTop={1}>
                <Typography component="div" variant="h5">Favourite Cities</Typography>
                <Divider />
                <Container 
                    sx={{
                        display: "flex",
                        flexFlow: "row wrap",
                        justifyContent: "space-evenly"
                    }}
                >
                    { favouriteCities.map((favouriteCity) => (
                        <Weather {...favouriteCity} onFavouriteCitiesChange={onFavouriteCitiesChange} />
                    ))}
                </Container>
            </Box>
        </>
    )
}

export default FavouriteCities;