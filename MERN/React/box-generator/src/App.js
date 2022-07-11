import React, { useState } from 'react';
import './App.css';
import DisplayBox from './components/DisplayBox';
import BoxForm from './components/BoxForm';

function App() {
    const boxes = [];

    const newBoxCreated = ( newBox ) => {
      boxes.push(newBox);
    }

  return (
    <div className="App">
        <BoxForm onCreateBox={ newBoxCreated }/>
        { boxes.map( (item, i) => 
            <DisplayBox boxColor={ item } key={i}/>
            )}
    </div>
  );
}

export default App;
