import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {

const [display, setDisplay] = useState(false);

  const [pokemon, setPokemon] = useState([]);

  useEffect(() => {
    fetch('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    .then(response => response.json())
    .then(response => setPokemon(response.results))
  }, []);


  const activeDisplay = () => {
    setDisplay(true);
  }


  return (
    <div>
      <button onClick={ activeDisplay }>Display Pokemon</button>
      <ul>
      {display === true && pokemon.length !== 0 && pokemon.map((pokemon, index) => {
        return(<li key={index}>{pokemon.name}</li>)
      })}
      </ul>
    </div>
  );
}

export default App;
