import React, { Component } from 'react';

class PersonCard extends Component{
    render(){
        const { lastName, firstName, age, color } = this.props
        return(
            <div>
                <h1>{ lastName }, { firstName }</h1>
                <p>Age: { age }</p>
                <p>Hair Color: { color }</p>
            </div>
        )
    }
}

export default PersonCard;