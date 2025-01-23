import React from 'react';
import './Styles.css'; // Centralized styles file

const RegisterPage = () => {
  return (
    <div className="page">
      <h1 className="page-title">Register</h1>
      <form className="form">
        <input type="text" placeholder="Username" className="form-input" />
        <input type="email" placeholder="Email" className="form-input" />
        <input type="password" placeholder="Password" className="form-input" />
        <button type="submit" className="form-button">Register</button>
      </form>
      <p className="login-redirect">
        Already have an account? <a href="/login" className="link">Log In</a>
      </p>
    </div>
  );
};

export default RegisterPage;
