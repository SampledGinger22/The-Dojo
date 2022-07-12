import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {

  const [display, setDisplay] = useState(false);

  const [pokemon, setPokemon] = useState([]);

  useEffect(() => {
    axios.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    .then(response=>{setPokemon(response.data.results)})
  }, []);

  const activeDisplay = () => {
    setDisplay(true);
    console.log(display);
  }

  return (
    <div>
      <button onClick={ activeDisplay }>Fetch Pokemon</button>
      <ul>
      {display === true && pokemon.length !== 0 && pokemon.map((pokemon, index) => {
        return(<li key={index}>{pokemon.name}</li>)
      })}
      </ul>
    </div>
  );
}

export default App;
