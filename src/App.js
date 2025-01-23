import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

// Pages
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import SitesPage from './pages/SitesPage';
import RegisterPage from './pages/RegisterPage';


function App() {
  return (
    <Router>
      <div className="app">
        <header className="header">
          <h1>Отсоеживание объектов культурного наследия</h1>
          <nav>
            <Link to="/">На главную</Link>
            <Link to="/about">О проекте</Link>
            <Link to="/register">Регистрация</Link>
            <Link to="/sites">Объекты</Link>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/sites" element={<SitesPage />} />
          </Routes>
        </main>
        <footer className="footer">
          <p>© 2025 Отсоеживание объектов культурного наследия</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
