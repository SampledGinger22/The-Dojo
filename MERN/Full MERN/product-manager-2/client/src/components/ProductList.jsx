import React from 'react';
import './style.css';
import { Link } from 'react-router-dom';

const ProductList = (props) => {

    return (
        <div className='bodycenter'>
            <div className='flexcolumn'>
                { props.products.map( (product, i) => 
                    <Link key={i} to={'/api/product/' + product._id}>{product.Title}</Link>
                )}
            </div>
        </div>
    )
}

export default ProductList;
