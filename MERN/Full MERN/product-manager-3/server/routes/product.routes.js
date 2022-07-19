const ProductController = require('../controller/product.controller');

module.exports = function(app){
    app.get('/api', ProductController.index);
    app.post('/api/products', ProductController.createProduct);
    app.get('/api/products/all', ProductController.getAllProducts);
    app.get('/api/product/:id', ProductController.getProduct);
    app.get('/api/product/:id/foredit', ProductController.getProduct);
    app.put('/api/product/:id/edit', ProductController.updateProduct);
}