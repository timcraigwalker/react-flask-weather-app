import './App.css';
import React from 'react';
import Search from './components/Search/search';

function App() {

  const handleOnSearchChange = (searchData) => {
    console.log(searchData);
  }
  

  return (
    <div className='body'>
      <div className='container'>
        <Search onSearchChange={handleOnSearchChange}/>
      </div>
    </div>
  );
}

export default App;
