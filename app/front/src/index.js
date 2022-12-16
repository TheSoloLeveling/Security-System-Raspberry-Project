import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import App from './App';
import LoginPage from './Login';
import { ContextProvider } from './contexts/ContextProvider';


ReactDOM.render(
  <React.StrictMode>
    <ContextProvider>
      
        <LoginPage></LoginPage>
      
    </ContextProvider>
  </React.StrictMode>,
  document.getElementById('root'),
);
