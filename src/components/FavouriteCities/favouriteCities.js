import { Box, Container, Divider, Typography } from "@mui/material";
import Weather from "../Weather/weather";

const FavouriteCities = ({favouriteCities}) => {

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
                        <Weather {...favouriteCity} />
                    ))}
                </Container>
            </Box>
        </>
    )
}

export default FavouriteCities;