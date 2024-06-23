// components/Search.js

import React, { useState } from 'react';
import axios from 'axios';

const Search = () => {
  const [query, setQuery] = useState('');
  const [rating, setRating] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await axios.post('/api/getRating', { query });
      setRating(response.data.rating);
      setError(null);
    } catch (error) {
      setError('An error occurred while fetching the rating.');
      setRating(null);
      console.error('Error fetching rating:', error);
    }
  };

  return (
    <div className="search-container">
      <input
        type="text"
        className="search-input"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter a query"
      />
      <button className="search-button" onClick={handleSearch}>
        Search
      </button>
      {rating && <div className="rating-output">Rating: {rating}</div>}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default Search;