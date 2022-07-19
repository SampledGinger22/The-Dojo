import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useParams, Link } from "react-router-dom";
    
const Update = (props) => {
    const { id } = useParams();
    const [title, setTitle] = useState('');
    const [price, setPrice] = useState('');
    const [description, setDescription] = useState('');
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/product/' + id)
            .then(res => {
                setTitle(res.data.Title);
                setPrice(res.data.Price);
                setDescription(res.data.Description)
            })
    }, []);
    
    const updateProduct = e => {
        e.preventDefault();
        console.log(title, price, description);
        axios.put('http://localhost:8000/api/product/' + id + '/edit', {
            Title: title,
            Price: price,
            Description: description
        })
            .then(res => console.log(res))
            .catch(err => console.error(err));
    }
    
    return (
        <div className='bodycenter'>
            <div className='flexcolumn'>
                <h1>Update a Product</h1>
                <Link to={ '/' }>Return to Home</Link>
                <form onSubmit={updateProduct}>
                    <p>
                        <label>Title</label><br />
                        <input type="text" 
                        name="title" 
                        value={title} 
                        onChange={(e) => { setTitle(e.target.value) }} />
                    </p>
                    <p>
                        <label>Price</label><br />
                        <input type="number" 
                        name="price"
                        value={price} 
                        onChange={(e) => { setPrice(e.target.value) }} />
                    </p>
                    <p>
                        <label>Description</label><br />
                        <input type="text" 
                        name="description"
                        value={description} 
                        onChange={(e) => { setDescription(e.target.value) }} />
                    </p>
                    <input type="submit" />
                </form>
            </div>
        </div>
    )
}
    
export default Update;

