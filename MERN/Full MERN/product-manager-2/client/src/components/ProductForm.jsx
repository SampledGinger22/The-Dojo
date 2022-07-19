import React, { useState } from 'react'
import axios from 'axios';
import './style.css';
export default () => {

    const [Title, setTitle] = useState(""); 
    const [Price, setPrice] = useState("");
    const [Description, setDescription] = useState("");

    const onSubmitHandler = e => {

        e.preventDefault();

        console.log('this is a test');

        

        axios.post('http://localhost:8000/api/products', {
            Title,
            Price,
            Description
        })
            .then(res=>console.log(res))
            .catch(err=>console.log(err))
    }

    return (
        <div className='bodycenter'>
            <div className='flexcolumn'>
                <h1>Product Manager</h1>
                <form onSubmit={onSubmitHandler}>
                    <p>
                        <label>Title</label><br/>
                        <input type="text" onChange={(e)=>setTitle(e.target.value)} value={Title}/>
                    </p>
                    <p>
                        <label>Price</label><br/>
                        <input type="number" onChange={(e)=>setPrice(e.target.value)} value={Price}/>
                    </p>
                    <p>
                        <label>Description</label><br/>
                        <input type="text" onChange={(e)=>setDescription(e.target.value)} value={Description}/>
                    </p>
                    <button type="submit">Create</button>
                </form>
            </div>
            <br/><br/><br/>
        </div>
    )
}

