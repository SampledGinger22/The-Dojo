const ProductController = require('../controller/product.controller');
module.exports = function(app){
    app.get('/api', ProductController.index);
    app.post('/api/people', ProductController.createProduct);
}