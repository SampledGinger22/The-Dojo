import React, { Component } from 'react';

class PersonCard extends Component{

    constructor(props){
        super(props);
        this.state = {
            age: this.props.age
        }
    }

    getOlder = () => {
        let age = this.state.age;
        age++;
        this.setState({age: age});
    }

    render(){
        let { lastName, firstName, age, color } = this.props
        return(
            <div>
                <h1>{ lastName }, { firstName }</h1>
                <p>Age: { this.state.age }</p>
                <p>Hair Color: { color }</p>
                <button onClick={ this.getOlder } >Birthday Button for {this.props.firstName} {this.props.lastName}</button>
            </div>
        )
    }
}

export default PersonCard;