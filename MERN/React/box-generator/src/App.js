import React, { useState } from 'react';
import './App.css';
import displayBox from './components/DisplayBox';
import boxForm from './components/BoxForm';

function App() {
    const boxes = [];

    const newBoxCreated = ( newBox ) => {
      boxes.push(newBox);
    }

  return (
    <div className="App">
        <boxForm onCreateBox={ newBoxCreated }/>
        { boxes.map( (item, i) => 
            <displayBox boxColor={ item } key={i}/>
            )}
    </div>
  );
}

export default App;
