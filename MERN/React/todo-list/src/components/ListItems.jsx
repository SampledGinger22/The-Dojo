import React from 'react';
import handleCompleteChange from '../App';
import Delete from '../App';

const DisplayToDos = (props) => {

    const { todoItem } = props;

    return (
        <div className='flexrow'>
            <input onChange={handleCompleteChange(props.i)} checked={props.complete} name="newItem" type="checkbox"></input>
            <label htmlFor="newItem" className='strikethrough'>{ props.text }</label>
            <button onClick={ Delete(props.i) }>Delete</button>
        </div>
    )
}

export default DisplayToDos;