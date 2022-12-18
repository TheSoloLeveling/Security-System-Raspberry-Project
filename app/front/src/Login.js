import React, { useState } from 'react'
import {Button, Form} from 'react-bootstrap'
import { Link } from 'react-router-dom'
import {useForm} from 'react-hook-form'
import 'bootstrap/dist/css/bootstrap.min.css'
import './main.css'
import { useNavigate } from 'react-router-dom'
import App  from './App'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Ecommerce, Orders, Calendar, Employees, Stacked, Pyramid, Customers, Kanban, Line, Area, Bar, Pie, Financial, ColorPicker, ColorMapping, Editor } from './pages';



const LoginPage=()=>{
    
    const {register,handleSubmit,reset,formState:{errors}}=useForm()
    const [isLogin, setIsLogin] = useState(false)
    
    const loginUser=(data)=>{
       console.log("data", data)

       const requestOptions={
           method:"POST",
           headers:{
               'content-type':'application/json'
           },
           body:JSON.stringify(data)
       }
        
       fetch('/auth/login',requestOptions)
       .then(res=>res.json())
       .then(data=>{
           console.log(data.access_token)
           
           if (data){
            //a = login(data.access_token)
            console.log(data.access_token)
            setIsLogin(true)

           }
           else{
               alert('Invalid username or password')
           }


       })

       reset()
    }

    return(
    <div>
        {isLogin ?
            <App/>
        :      
        <div className="container">
            <div className="form">
                <h1>Admin Login</h1>
                <form>
                    <Form.Group>
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text"
                            placeholder="Your username"
                            {...register('username',{required:true,maxLength:25})}
                        />
                    </Form.Group>
                    {errors.username && <p style={{color:'red'}}><small>Username is required</small></p>}
                    {errors.username?.type === "maxLength" && <p style={{color:'red'}}><small>Username should be 25 characters</small></p>}
                    <br></br>
                
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password"
                            placeholder="Your password"
                            {...register('password',{required:true,minLength:8})}
                        />
                    </Form.Group>
                    {errors.username && <p style={{color:'red'}}><small>Password is required</small></p>}
                    {errors.password?.type === "maxLength" && <p style={{color:'red'}}>
                        <small>Password should be more than 8 characters</small>
                        </p>}
                    <br></br>
                    <Form.Group>
                        <Button as="sub" variant="primary" onClick={handleSubmit(loginUser)}>Login</Button>
                    </Form.Group>
                    <br></br>
                    
                </form>
            </div>
        </div>
        
        }
        
    </div>
    
    )




}

export default LoginPage