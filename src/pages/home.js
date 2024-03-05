import React, { useEffect, useState } from "react";

import { Container, CssBaseline } from "@mui/material";
import { useNavigate } from "react-router-dom";
import FavouriteCities from "../components/FavouriteCities/favouriteCities";
import Search from "../components/Search/search";
import SearchedCity from "../components/SearchedCity/searchedCity";

const Home = ({user}) => {
    const navigate = useNavigate();
    const [searchValues, setSearchValues] = useState(null);
    const [favouriteCities, setFavouriteCities] = useState(null);

    const handleOnSearchChange = (searchData) => {
        const [latitude, longitude] = searchData.value.split(" ");

        setSearchValues({
          user: user.id,
          city: searchData.label,
          latitude: latitude,
          longitude: longitude
        });
    };

    const handleUserFavouriteCitiesChange = (changed) => {
      console.log(changed);
      getUserFavouriteCities(user);
    }

    const getUserFavouriteCities = async (user) => {
      try {
        const favouriteCitiesResponse = await fetch(`api/user/${user.id}/favourite_cities`);
        const favouriteCitiesResponseJson = await favouriteCitiesResponse.json();

        if(favouriteCitiesResponse.status === 200){
          setFavouriteCities(favouriteCitiesResponseJson);
        }
      } catch (error) {
        console.error(error);
      }
    }

    useEffect(() => {
      if(!user || !user.id) navigate("/login");
      if(!favouriteCities) getUserFavouriteCities(user);
      // TODO: find out why this is looping
    }, [favouriteCities, navigate, user]);

    return (
      <>
        <Container component="main" maxWidth="xl">
          <CssBaseline />
          <Search onSearchChange={handleOnSearchChange}/>
          { searchValues  && <SearchedCity searchValues={searchValues} />}
          { favouriteCities  && <FavouriteCities favouriteCities={favouriteCities} onFavouriteCitiesChange={handleUserFavouriteCitiesChange} />}
        </Container>
      </>
    );
  }
  
  export default Home;