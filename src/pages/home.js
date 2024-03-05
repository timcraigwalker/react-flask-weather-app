import React, { useEffect, useState } from "react";

import { Container, CssBaseline } from "@mui/material";
import { useDispatch, useSelector } from "react-redux";
import FavouriteCities from "../components/FavouriteCities/favouriteCities";
import Search from "../components/Search/search";
import SearchedCity from "../components/SearchedCity/searchedCity";
import { fetchFavouriteCities } from "../redux/slices/userFavouriteCitiesSlice";

const Home = () => {
    const dispatch = useDispatch();
    const user = useSelector((state) => state.user.data);
    const favouriteCities = useSelector((state) => state.userFavouriteCities.data);
    
    const [searchValues, setSearchValues] = useState(null);

    const handleOnSearchChange = (searchData) => {
        const [latitude, longitude] = searchData.value.split(" ");

        setSearchValues({
          city: searchData.label,
          latitude: latitude,
          longitude: longitude
        });
    };

    useEffect(() => {
      dispatch(fetchFavouriteCities(user));
    }, [dispatch, user]);

    return (
      <>
        <Container component="main" maxWidth="xl">
          <CssBaseline />
          <Search onSearchChange={handleOnSearchChange}/>
          { searchValues  && <SearchedCity searchValues={searchValues} />}
          { (favouriteCities && favouriteCities.length !== 0) && <FavouriteCities favouriteCities={favouriteCities} />}
        </Container>
      </>
    );
  }
  
  export default Home;