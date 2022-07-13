import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import SearchBar from './components/searchBar';
import axios from 'axios';

function App() {
  
  const [ SearchList, setSearchList ] = useState([]);
  const [ SearchId, setSearchId ] = useState('');
  const [ SearchParam, setSearchParam ] = useState('people');

  const onNewSearch = (Id, Param) => {
    setSearchList([]);
    setSearchId(Id);
    setSearchParam(Param);
    console.log(SearchList);
  }

  useEffect(() => {
    axios.get("https://swapi.dev/api/${SearchParam}/${SearchId}")
    .then(response => {setSearchList(response.data)})
    .then(response => console.log(response.data))
  }, [SearchParam, SearchId]);


  return (
    <div className='App'>
      <SearchBar onNewSearch={ onNewSearch }/>
    </div>
  );
}

export default App;
