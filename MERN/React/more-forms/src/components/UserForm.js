import React, { useState } from 'react';


const UserForm = (props) => {
    const [firstName, setfirstName] = useState("");
    const [firstNameError, setfirstNameError] = useState("");
    const [lastName, setlastName] = useState("");
    const [lastNameError, setlastNameError] = useState("");
    const [email, setEmail] = useState("");
    const [EmailError, setEmailError] = useState("");
    const [password, setPassword] = useState("");
    const [PasswordError, setPasswordError] = useState("");
    const [confPassword, setconfPassword] = useState("");
    const [confPasswordError, setconfPasswordError] = useState("");

    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstName, lastName, email, password, confPassword };
        console.log("Welcome", newUser);
    };

    const validateFirstName = (e) => {
        setfirstName(e.target.value);
        if(e.target.value.length < 1){
            setfirstNameError("First Name is Required");
        }
        else if(e.target.value.length < 2){
            setfirstNameError("First Name Must be at Least Two Characters Long");
        }
        else setfirstNameError('');
    }

    const validateLastName = (e) => {
        setlastName(e.target.value);
        if(e.target.value.length < 1){
            setlastNameError("Last Name is Required");
        }
        else if(e.target.value.length < 2){
            setlastNameError("Last Name Must be at Least Two Characters Long");
        }
        else setlastNameError('');
    }

    const validateEmail = (e) => {
        setEmail(e.target.value);
        if(e.target.value.length < 1){
            setEmailError("Email is Required");
        }
        else if(e.target.value.length < 5){
            setEmailError("Email Must be at Least Five Characters Long");
        }
        else setEmailError('');
    }

    const validatePassword = (e) => {
        setPassword(e.target.value);
        if(e.target.value.length < 1){
            setPasswordError("Password is Required");
        }
        else if(e.target.value.length < 8){
            setPasswordError("Password Must be at Least Eight Characters Long");
        }
        else setPasswordError('');
    }

    const validateconfPassword = (e) => {
        setconfPassword(e.target.value);
        if(e.target.value != password){
            setconfPasswordError("Passwords Do Not Match");
        }
        else setconfPasswordError('');
    }

    return (
        <form onSubmit={createUser}>
            <div>
                <label>First Name: </label>
                <input type="text" onChange={ validateFirstName } />
                {
                    firstNameError ?
                    <p style={{ color: "red" }}>{ firstNameError }</p> :
                    ''
                }
            </div>
            <div>
                <label>Last Name: </label>
                <input type="text" onChange={ validateLastName} />
                {
                    lastNameError ?
                    <p style={{ color: "red" }}>{ lastNameError }</p> :
                    ''
                }
            </div>
            <div>
                <label>Email Address: </label>
                <input type="text" onChange={ validateEmail } />
                {
                    EmailError ?
                    <p style={{ color: "red" }}>{ EmailError }</p> :
                    ''
                }
            </div>
            <div>
                <label>Password: </label>
                <input type="text" onChange={ validatePassword } />
                {
                    PasswordError ?
                    <p style={{ color: "red" }}>{ PasswordError }</p> :
                    ''
                }
            </div>
            <div>
                <label>Confirm Password: </label>
                <input type="text" onChange={ validateconfPassword } />
                {
                    confPasswordError ?
                    <p style={{ color: "red" }}>{ confPasswordError }</p> :
                    ''
                }
            </div>
            <input type="submit" value="Create User" />
        </form>
    );
};

export default UserForm;
