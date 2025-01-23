import React from 'react';
import { Link } from 'react-router-dom';
import './Styles.css';

const HomePage = () => {
  return (
    <div className="homepage">
      <section className="intro">
        <h2>Welcome to Cultural Heritage Tracker</h2>
        <p>
          Explore and preserve Russia's rich cultural heritage. Monitor the status of historical sites, receive real-time updates, and contribute to preservation efforts.
        </p>
        <Link to="/register" className="cta-button">Get Started</Link>
      </section>
      <section className="why-it-matters">
        <h3>Why It Matters</h3>
        <p>
          Cultural heritage sites are more than monuments; they are windows into our history, art, and traditions. Help us protect these treasures for future generations.
        </p>
      </section>
      <section className="features">
        <h3>Features</h3>
        <ul>
          <li>Track and monitor cultural sites in real-time.</li>
          <li>Receive notifications on changes or threats to sites.</li>
          <li>Search for sites with an intuitive live search feature.</li>
          <li>View detailed information and map locations.</li>
        </ul>
      </section>
      <section className="how-it-works">
        <h3>How It Works</h3>
        <ol>
          <li>Sign up and create your account.</li>
          <li>Search for and select cultural sites to monitor.</li>
          <li>Receive notifications and updates about site status.</li>
          <li>Engage with the community to support preservation efforts.</li>
        </ol>
      </section>
    </div>
  );
};

export default HomePage;
