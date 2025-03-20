import React, { useEffect, useState } from "react";
import axios from "axios";
import "./ChangesPage.css";

const ChangesPage = () => {
  const [changes, setChanges] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchChanges = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/changes/");
        setChanges(response.data);
      } catch (error) {
        console.error("Error fetching changes:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchChanges();
  }, []);

  if (isLoading) {
    return <p>Loading changes...</p>;
  }

  return (
    <div className="changes-page">
      <h1>Cultural Heritage Site Changes</h1>
      {changes.length === 0 ? (
        <p>No changes found.</p>
      ) : (
        <table className="changes-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Object Name</th>
              <th>Change Type</th>
              <th>Category</th>
              <th>Location</th>
              <th>Security Status</th>
            </tr>
          </thead>
          <tbody>
            {changes.map((change) => (
              <tr key={change.id}>
                <td>{change.id}</td>
                <td>{change.ObjectNameOnDoc}</td>
                <td>{change.change_type}</td>
                <td>{change.Category}</td>
                <td>{change.Location}</td>
                <td>{change.SecurityStatus}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ChangesPage;
