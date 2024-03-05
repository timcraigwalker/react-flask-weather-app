import { Box, Container } from "@mui/material";
import Weather from "../Weather/weather";

const SearchedCity = ({searchValues}) => {

    console.log(searchValues);

    return (
        <>
            <Box marginTop={1}>
                <Container 
                    sx={{
                        display: "flex",
                        flexFlow: "row",
                        justifyContent: "center"
                    }}
                >
                    { searchValues && <Weather {...searchValues} />}
                </Container>
            </Box>
        </>
    )
}

export default SearchedCity;