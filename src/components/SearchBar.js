import React, { useState, useEffect } from "react";
import axios from "axios";

const SearchBar = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  
  useEffect(() => {
    const fetchResults = async () => {
      if (query.length > 2) {
        const response = await axios.get(
          `http://localhost:8000/api/search?q=${query}`
        );
        setResults(response.data);
      }
    };

    const debounce = setTimeout(fetchResults, 500);

    return () => clearTimeout(debounce);  // Clean up debounce
  }, [query]);

  return (
    <div>
      <input
        type="text"
        placeholder="Search for cultural heritage sites"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul>
        {results.map((result) => (
          <li key={result.id}>{result.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchBar;
