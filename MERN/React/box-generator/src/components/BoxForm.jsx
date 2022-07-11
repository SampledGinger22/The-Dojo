import React, { useState } from 'react';

const BoxForm = props => {

    const [boxColor, setboxColor] = useState("");

    const createBox = (e) => {
        e.preventDefault();
        props.onCreateBox( boxColor );
    }

    return (
        <form onSubmit={createBox}>
            <div>
                <label>Color:</label>
                <input type="text" onChange={(e) => setboxColor(e.target.value)}></input>
                <button type="submit">Add</button>
            </div>
        </form>
    );
}

export default BoxForm;