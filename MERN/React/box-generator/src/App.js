import React from 'react';
import './App.css';
import DisplayBox from './components/DisplayBox';
import BoxForm from './components/BoxForm';
import './components/Style.css'

function App() {
    const boxes = [];

    const newBoxCreated = ( newBox ) => {
      boxes.push(newBox);
      console.log(newBox);
    }

  return (
    <div className='flexcolumn'>
      <div className="App">
          <BoxForm onCreateBox={ newBoxCreated }/>
          <div className='flexrow'>
          { boxes.map( (item, i) => 
              <DisplayBox color={ item } key={i}/>
              ) }
          </div>
      </div>
    </div>
  );
}

export default App;
