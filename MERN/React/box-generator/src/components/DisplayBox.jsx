import React from 'react';
import './Style.css'

const DisplayBox = (props) => {
    return (
        <div className="styledbox" style={{backgroundColor: props.boxColor}}></div>
    );
}

export default DisplayBox;