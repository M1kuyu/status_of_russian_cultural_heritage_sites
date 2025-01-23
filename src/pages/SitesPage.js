import React, { useState, useEffect } from 'react';
import './Styles.css'; // Centralized styles file

const SitesPage = () => {
  const [sites, setSites] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  // Fetch sites from the API
  useEffect(() => {
    const fetchSites = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/sites/");
        const data = await response.json();
        setSites(data); // Save the API response in the state
      } catch (error) {
        console.error("Error fetching sites:", error);
      }
    };
    fetchSites();
  }, []);

  // Filter sites based on search term
  const filteredSites = sites.filter((site) =>
    site.ObjectNameOnDoc?.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="page">
      <h1 className="page-title">Cultural Heritage Sites</h1>
      <input
        type="text"
        placeholder="Search sites..."
        className="search-input"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <div className="site-list">
        {filteredSites.length > 0 ? (
          filteredSites.map((site) => (
            <div key={site.id} className="site-card">
              <h3>{site.ObjectNameOnDoc}</h3>
              <p><strong>Category:</strong> {site.Category || "N/A"}</p>
              <p><strong>Location:</strong> {site.Location || "N/A"}</p>
              <p><strong>Security Status:</strong> {site.SecurityStatus || "N/A"}</p>
            </div>
          ))
        ) : (
          <p>No sites found.</p>
        )}
      </div>
    </div>
  );
};

export default SitesPage;
