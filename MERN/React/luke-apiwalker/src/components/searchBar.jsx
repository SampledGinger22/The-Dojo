import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './style.css';

const SearchBar = (props) => {
    
    const handleSubmit = (e) => {
        e.preventDefault();
        props.onNewSearch(Id, Param);
        e.target.reset();
    }

    const [Id, setId] = useState('');
    const [Param, setParam] = useState('');

    return (
        <div className='flexrow spacefromtop'>
            <form className='ui form' onSubmit={ handleSubmit } >
                <div className='fields'>
                    <div className='field'>
                        <label>Search for: </label>
                        <select className='us fluid dropdown' onChange={(e) => setParam(e.target.value)}>
                            <option value='' defaultValue hidden></option>
                            <option value={'people'}>People</option>
                            <option value={'planets'}>Planets</option>
                        </select>
                    </div>
                    <div className='field'>
                        <label>Id Number: </label>
                        <input onChange={(e) => setId(e.target.value)} placeholder='id' maxLength={2} type='number'/>
                    </div>
                </div>
                <button type='submit' className='ui button'>Search</button>
            </form>
        </div>
    )
}

export default SearchBar;