const mongoose = require('mongoose');

 
const JokeSchema = new mongoose.Schema({
    _id: {
        type: mongoose.Schema.ObjectId, 
        auto: true
    },
    setup: { 
        type: String,
        required: [true, "Must have a setup"],
        maxlength: [10, "Setup must be at least ten characters long"]
    },
    punchline: {
        type: String,
        required: [true, "Must have a punchline"],
        maxlength: [3, "Punchline must be at least three characters long"]
    },
    createdAt: { type: Date, required: true, default: Date.now },
    updatedAt: { type: Date, required: true, default: Date.now }
});
 
const Joke = mongoose.model('Joke', JokeSchema);
 
module.exports = Joke;
