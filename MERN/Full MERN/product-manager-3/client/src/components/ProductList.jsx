import React from 'react';
import './style.css';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const ProductList = (props) => {

    const {removeFromDom} = props;
    const navigate = useNavigate();

    const deleteProduct = (productId) => {
        axios.delete('http://localhost:8000/api/product/' + productId + '/delete')
            .then(res => {
                removeFromDom(productId)
            })
            .catch(err => console.error(err));
        navigate(0);
    }

    return (
        <div className='bodycenter'>
            <div className='flexcolumn'>
                { props.products.map( (product, i) => 
                    <p>
                    <Link key={i} to={'/api/product/' + product._id}>{product.Title}</Link>
                    <button className='margin-left-5' onClick={(e) => {deleteProduct(product._id)}}>Delete</button>
                    </p>
                )}
            </div>
        </div>
    )
}

export default ProductList;
