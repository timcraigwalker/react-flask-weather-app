import React from "react";

import Search from "../components/Search/search";
import CurrentWeather from "../components/CurrentWeather/currentWeather";

const Home = () => {

    const handleOnSearchChange = (searchData) => {
      console.log(searchData);
    }
    
  
    return (
      <div className='body'>
        <div className='container'>
          <Search onSearchChange={handleOnSearchChange}/>
          <CurrentWeather />
        </div>
      </div>
    );
  }
  
  export default Home;