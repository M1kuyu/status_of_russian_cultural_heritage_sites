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
          <h1>Cultural Heritage Tracker</h1>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/register">Get Started</Link>
            <Link to="/Sites">Sites</Link>
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
          <p>© 2025 Cultural Heritage Tracker. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
