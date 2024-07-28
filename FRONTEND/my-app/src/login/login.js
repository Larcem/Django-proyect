import React, { useState } from 'react';
import './login.css';

    function Login() {
    const [usuario, setUsuario] = useState('');
    const [contrasena, setContrasena] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Usuario:', usuario);
        console.log('Contraseña:', contrasena);
    };

    return (
        <div className="login-container">
        <div className="login-form">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
            <div>
                <label>Usuario:</label>
                <input
                type="text"
                value={usuario}
                onChange={(e) => setUsuario(e.target.value)}
                required
                />
            </div>
            <div>
                <label>Contraseña:</label>
                <input
                type="password"
                value={contrasena}
                onChange={(e) => setContrasena(e.target.value)}
                required
                />
            </div>
            <button type="submit">Login</button>
            </form>
        </div>
        </div>
    );
    }

    export default Login;
