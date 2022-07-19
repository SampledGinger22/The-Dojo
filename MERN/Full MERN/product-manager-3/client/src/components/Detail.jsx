import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useParams, Link, useNavigate } from "react-router-dom";
import './style.css';


const Detail = (props) => {
    
    const [product, setProduct] = useState({})
    const { id } = useParams();
    const navigate = useNavigate();
    const {removeFromDom} = props;
    
    useEffect(() => {
        axios.get('http://localhost:8000/api/product/' +id)
            .then(res => setProduct(res.data))
            .catch(err => console.error(err));
    }, []);

    const deleteProduct = (productId) => {
        axios.delete('http://localhost:8000/api/product/' + productId + '/delete')
            .then(res => {
                removeFromDom(productId)
            })
            .catch(err => console.error(err));
        navigate('/');
    }
    
    return (
        <div className='bodycenter'>
            <div className='flexcolumn'>
                <p>Title: {product.Title}</p>
                <p>Price: {product.Price}</p>
                <p>Description: { product.Description }</p>
            </div>
            <Link to={"/api/product/" + id + "/foredit"}>Edit</Link>
            <Link to={ '/' }>Return to Home</Link>
            <button onClick={(e) => {deleteProduct(id)}}>Delete</button>
        </div>
    )
}

export default Detail;

