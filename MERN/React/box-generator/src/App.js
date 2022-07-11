import React, { useState } from 'react';
import './App.css';
import DisplayBox from './components/DisplayBox';
import BoxForm from './components/BoxForm';
import './components/Style.css'

function App() {
  
    const [BoxColor, setBoxColor] = useState([]);

    const newBoxCreated = (e, boxColor ) => {
      e.preventDefault();
      if(boxColor.length > 2){
        setBoxColor([...BoxColor, boxColor]);
      }
    }

  return (
    <div className='flexcolumn'>
      <div className="App">
          <BoxForm newBoxCreated={ newBoxCreated }/>
          <div className='flexrow'>
          { BoxColor.map( (boxColor, i) => 
              <DisplayBox boxColor={boxColor} key={i}/> ) }
          </div>
      </div>
    </div>
  );
}

export default App;
