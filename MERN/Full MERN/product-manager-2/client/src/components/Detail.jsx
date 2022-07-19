import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useParams } from "react-router-dom";
import './style.css';


const Detail = (props) => {
    
    const [product, setProduct] = useState({})
    const { id } = useParams();
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/product/' +id)
            .then(res => setProduct(res.data))
            .catch(err => console.error(err));
    }, []);
    
    return (
        <div className='bodycenter'>
            <div className='flexcolumn'>
                <p>Title: {product.Title}</p>
                <p>Price: {product.Price}</p>
                <p>Description: { product.Description }</p>
            </div>
        </div>
    )
}

export default Detail;

