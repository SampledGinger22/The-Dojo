import React from 'react';
import './Style.css'

const DisplayBox = (props) => {
    return (
        <div className="styledbox" style={{background: props.color}} ></div>
    );
}

export default DisplayBox;