import './App.css';
import React from 'react';

import CurrentWeather from './components/CurrentWeather/currentWeather';
import Header from './components/Header/header'
import Search from './components/Search/search';

function App() {

  const handleOnSearchChange = (searchData) => {
    console.log(searchData);
  }
  

  return (
    <div className='body'>
      <Header />
      <div className='container'>
        <Search onSearchChange={handleOnSearchChange}/>
        <CurrentWeather />
      </div>
    </div>
  );
}

export default App;
