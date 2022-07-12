import React, { useState } from 'react';
import './Style.css';

const ListForm = (props) => {

    const handleSubmit = (e) => {
        e.preventDefault();
    
        if(item){
            props.onNewItem(item);
            e.target.reset();
        }
    }

    const [item, setItem] = useState("");

    return (
        <form id='newitem' onSubmit={ handleSubmit } className="flexrow">
            <label>Create New To-Do:</label>
            <input type="text" onChange={(e) => setItem(e.target.value)}/>
            <button type="submit">Add</button>
        </form>
    );
}

export default ListForm;