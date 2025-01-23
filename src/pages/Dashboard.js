import React, { useState, useEffect } from "react";
import axios from "axios";

const Dashboard = () => {
  const [trackedObjects, setTrackedObjects] = useState([]);

  useEffect(() => {
    const fetchTrackedObjects = async () => {
      const token = localStorage.getItem("token");
      const response = await axios.get("http://localhost:8000/api/tracked", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setTrackedObjects(response.data);
    };
    fetchTrackedObjects();
  }, []);

  return (
    <div>
      <h2>Your Tracked Cultural Sites</h2>
      <ul>
        {trackedObjects.map((obj) => (
          <li key={obj.id}>
            <h4>{obj.name}</h4>
            <p>{obj.status}</p>
            <button>View Details</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
