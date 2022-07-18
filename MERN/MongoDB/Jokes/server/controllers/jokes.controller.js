const Joke = require('../models/jokes.model');
 
module.exports.findAllJokes = (req, res) => {
    Joke.find()
        .then(allDaJokes => res.json({ jokes: allDaJokes }))
        .catch(err => res.json({ message: 'Something went wrong', error: err }));
}
 
module.exports.findOneSingleJoke = (req, res) => {
    Joke.findOne({ _id: req.params._id })
        .then(oneSingleJoke => res.json({ joke: oneSingleJoke }))
        .catch(err => res.json({ message: 'Something went wrong', error: err }));
}

module.exports.findRandomJoke = (req, res) => {
    Joke.aggregate([{$sample: { size: 1 }}])
        .then(oneRandomJoke => res.json({ joke: oneRandomJoke}))
        .catch(err => res.json({ message: 'Something went wrong', error: err }));
}
 
module.exports.createNewJoke = (req, res) => {
    Joke.create(req.body)
        .then(newlyCreatedJoke => res.json({ joke: newlyCreatedJoke }))
        .catch(err => res.json({ message: 'Something went wrong', error: err }));
}
 
module.exports.updateExistingJoke = (req, res) => {
    Joke.findOneAndUpdate(
        { _id: req.params._id },
        req.body,
        { new: true, runValidators: true }
    )
        .then(updatedJoke => res.json({ joke: updatedJoke }))
        .catch(err => res.json({ message: 'Something went wrong', error: err }));
}
 
module.exports.deleteAnExistingJoke = (req, res) => {
    Joke.deleteOne({ _id: req.params._id })
        .then(result => res.json({ result: result }))
        .catch(err => res.json({ message: 'Something went wrong', error: err }));
}

