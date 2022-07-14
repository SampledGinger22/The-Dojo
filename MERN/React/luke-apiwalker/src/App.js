import './App.css';
import React, { useState } from 'react';
import SearchBar from './components/searchBar';
import axios from 'axios';
import { Routes, Route, useNavigate } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Welcome!</h1>
    </div>
  )
}

const Err = () => {
  return (
    <div>
      <h1>These are not the droids you're looking for.</h1>
    </div>
  )
}

const DisplayPeople = (props) => {

  const { SearchList } = props;

  return (
    <div className='flexcolumn'>
      <h1>{SearchList.name}</h1>
      <br />
      <h3>Height: {SearchList.height}</h3>
      <h3>Mass: {SearchList.mass}</h3>
      <h3>Hair Color: {SearchList.hair_color}</h3>
      <h3>Skin Color: {SearchList.skin_color}</h3>
    </div>
  );
}

const DisplayPlanets = (props) => {

  const { SearchList } = props;

  return (
    <div className='flexcolumn'>
      <h1>{SearchList.name}</h1>
      <br />
      <h3>Climate: {SearchList.climate}</h3>
      <h3>Terrain: {SearchList.terrain}</h3>
      <h3>Surface Water: {SearchList.surface_water}</h3>
      <h3>Population: {SearchList.population}</h3>
    </div>
  );
}

function App() {
  
  const [ SearchList, setSearchList ] = useState('');

  const navigate = useNavigate();

  const onNewSearch = (Id, Param) => {
    console.log(Id, Param);
    axios.get('https://swapi.dev/api/' + Param + '/' + Id)
    .then(response => {setSearchList(response.data)})
    .then(Param === "people" ? navigate("/people/display") 
    : navigate("/planets/display"))
    .catch(err => {navigate("/err")});
  }


  return (
    <div>
      <SearchBar onNewSearch={ onNewSearch }/>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/err" element={<Err />}/>
        <Route path="/people/display" element={<DisplayPeople SearchList={ SearchList } />}/>
        <Route path="/planets/display" element={<DisplayPlanets SearchList={ SearchList } />}/>
      </Routes>
    </div>
  );
}

export default App;
