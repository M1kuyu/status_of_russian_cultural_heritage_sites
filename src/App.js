import './App.css'; // Add this line at the top of your App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import SearchBar from "./components/SearchBar";
//import Map from "./components/Map";

const App = () => {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Cultural Heritage Tracker</h1>
          <nav>
            <Link to="/register">Register</Link>
            <Link to="/login">Login</Link>
            <Link to="/dashboard">Dashboard</Link>
          </nav>
        </header>

        <div className="main-content">
          <SearchBar />
          <Routes>
            <Route path="/register" element={<Register />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/" element={<div>Welcome to the Cultural Heritage Tracker</div>} />
          </Routes>
        </div>

        <footer>
          <p>2025 © Cultural Heritage Tracker</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
