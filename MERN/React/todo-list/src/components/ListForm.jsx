import React, { useState } from 'react';
import './Style.css';
import handleSubmit from '../App';

const ListForm = (props) => {

    const {handleSubmit} = props;

    const [Item, setItem] = useState("");

    return (
        <form id='newitem' onSubmit={(e) => handleSubmit(e, Item)} className="flexrow">
            <label>Create New To-Do:</label>
            <input type="text" onChange={(e) => setItem(e.target.value)}></input>
            <button type="submit">Add</button>
        </form>
    );
}

export default ListForm;