import React, { useState } from 'react';

const BoxForm = (props) => {

    const {newBoxCreated} = props;

    const [boxColor, setboxColor] = useState("");

    return (
        <form onSubmit={(e) => newBoxCreated(e, boxColor)}>
            <label>Color:</label>
            <input type="text" onChange={(e) => setboxColor(e.target.value)}></input>
            <button type="submit">Add</button>
        </form>
    );
}

export default BoxForm;