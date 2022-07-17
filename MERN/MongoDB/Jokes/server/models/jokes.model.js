const mongoose = require('mongoose');
 
const JokeSchema = new mongoose.Schema({
    _id: Number,
    setup: String,
    punchline: String
});
 
const Joke = mongoose.model('Joke', JokeSchema);
 
module.exports = Joke;
