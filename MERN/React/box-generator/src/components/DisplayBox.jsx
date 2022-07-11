import React from 'react';
import './Style.css'

const DisplayBox = (color) => {
    return (
        <div className="styledbox" style={{background: color}} ></div>
    );
}

export default DisplayBox;