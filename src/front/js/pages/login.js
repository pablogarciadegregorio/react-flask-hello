import React, { useState, useEffect, useContext }  from "react";

import { Context } from "../store/appContext";
import "../../styles/home.css";
import { useNavigate } from "react-router-dom";



export const Login = () => {
    
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const { store, actions } = useContext(Context);
    const navigate = useNavigate();

    async function handleSubmit(e) {
        e.preventDefault();
        
        let logged = await actions.login(email,password); // guardamos el booleano que devuelve el awaiten logged
        if (logged) { //true
            navigate("/")       // si logeas bien te redirige a la pagina principal
        }

        //false
        setEmail("");
        setPassword("");
    }

    return (
        <>
        <form className="w-50 m-auto" onSubmit={handleSubmit}>
            <h1 className="mx-auto">LOGIN</h1>
            <div className="form-group mt-3">
                <label for="exampleInputEmail1 mb-2">Email address</label>
                <input type="email" className="form-control mb-2" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" onChange={(e)=> setEmail(e.target.value)}></input>
                    <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
            <div className="form-group mt-3">
                <label for="exampleInputPassword1 mb-2">Password</label>
                <input type="password mb-2" className="form-control" id="exampleInputPassword1" placeholder="Password" onChange={(e)=> setPassword(e.target.value)}></input>
            </div>
            
            <button type="submit" className="btn btn-primary mt-3">Submit</button>
        </form>
        </>
    )




}