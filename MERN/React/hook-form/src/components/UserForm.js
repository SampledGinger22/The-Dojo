import React, { useState } from 'react';


const UserForm = (props) => {
    const [firstName, setfirstName] = useState("");
    const [lastName, setlastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confPassword, setconfPassword] = useState("");

    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstName, lastName, email, password, confPassword };
        console.log("Welcome", newUser);
    };

    const newUser = { firstName, lastName, email, password, confPassword };

    return (
        <form onSubmit={createUser}>
            <div>
                <label>First Name: </label>
                <input type="text" onChange={(e) => setfirstName(e.target.value)} />
            </div>
            <div>
                <label>Last Name: </label>
                <input type="text" onChange={(e) => setlastName(e.target.value)} />
            </div>
            <div>
                <label>Email Address: </label>
                <input type="text" onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div>
                <label>Password: </label>
                <input type="text" onChange={(e) => setPassword(e.target.value)} />
            </div>
            <div>
                <label>Confirm Password: </label>
                <input type="text" onChange={(e) => setconfPassword(e.target.value)} />
            </div>
            <input type="submit" value="Create User" />
            <div>
                <h1>Your Form Data</h1>
                <p>First Name: { newUser.firstName }</p>
                <p>Last Name: { newUser.lastName }</p>
                <p>Email: { newUser.email }</p>
                <p>Password: { newUser.password }</p>
                <p>Password Confirmation: { newUser.confPassword }</p>
            </div>
        </form>
    );
};

export default UserForm;
