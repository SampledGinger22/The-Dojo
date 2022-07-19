const { Product } = require('../models/product.model');
module.exports.index = (request, response) => {
    response.json({
        message: "Hello World"
    });
}

module.exports.createProduct = (request, response) => {
    const { Title, Price, Description } = request.body;
    Product.create({
        Title,
        Price,
        Description
    })
        .then(product => response.json(product))
        .catch(err => response.json(err));
}