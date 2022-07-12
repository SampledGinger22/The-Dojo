import React from 'react';
import './Style.css';

const DisplayToDos = (props) => {

    const { todoItem, idx } = props;

    const handleDelete = () => {
        console.log(idx);
        props.onDeletion(idx);
    }

    return (
        <div className='flexrow'>
            <input name="newItem" type="checkbox"></input>
            <label htmlFor="newItem" className='strikethrough'>{ todoItem }</label>
            <button onClick={ handleDelete }>Delete</button>
        </div>
    )
}

export default DisplayToDos;