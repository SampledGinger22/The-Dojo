import React, { useState } from 'react';

const Tab = (props) => {

    const [Button, NewButton] = useState('');
    const [String, NewString] = useState('');

    const newTab = (arr = []) => {
        arr.map()
    }

    return (
        <button type='button' onClick={newTab}>Tab { props.ArrNum }</button>
    )
}