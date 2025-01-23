import React, { useState } from 'react';
import './Styles.css'; // Centralized styles file

const RegisterPage = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Prepare the data to be sent to the API
    const userData = {
      username,
      password,
      email, // Assuming you want to include email in the registration
    };

    try {
      const response = await fetch('http://localhost:8000/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }

      const data = await response.json();
      setMessage(data.message); // Display success message
    } catch (error) {
      setMessage(error.message); // Display error message
    }
  };

  return (
    <div className="page">
      <h1 className="page-title">Регистрация</h1>
      <form className="form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          className="form-input"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          className="form-input"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          className="form-input"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit" className="form-button">Register</button>
      </form>
      {message && <p className="message">{message}</p>}
      <p className="login-redirect">
        Уже Зарегистрирированы? <a href="/login" className="link">Log In</a>
      </p>
    </div>
  );
};

export default RegisterPage;
