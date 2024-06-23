import React, { useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [query, setQuery] = useState('');
  const [rating, setRating] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await axios.post('/api/getRating', { query });
      setRating(response.data.rating);
      setError(null);
    } catch (err) {
      setError('An error occurred while fetching the rating.');
      setRating(null);
    }
  };

  const handleExampleClick = (example) => {
    setQuery(example);
    handleSearch();
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="bg-white shadow-md rounded-lg p-8 w-full max-w-2xl">
        <h1 className="text-4xl font-bold text-gray-900 mb-4 text-center">Welcome to my Weaviate Sample Project</h1>
        <p className="text-gray-700 mb-8 text-center">Enter a rating below to get the model's predicted rating (1-5).</p>
        <div className="search-container flex flex-col items-center">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="search-input p-2 border border-gray-300 rounded mb-4 w-full max-w-md"
            placeholder="Enter your review here"
          />
          <button onClick={handleSearch} className="search-button bg-blue-500 text-white p-2 rounded w-full max-w-md">
            Submit
          </button>
          <div className="examples mt-6">
            <p className="text-gray-700 mb-2">Example Inputs:</p>
            <button onClick={() => handleExampleClick("This product was okay. It fit me fairly well but was too costly")} className="example-button bg-gray-200 text-blue-500 p-2 rounded mb-2 w-full max-w-md">
              This product was okay. It fit me fairly well but was too costly
            </button>
            <button onClick={() => handleExampleClick("This product was terrible! I am never buying this again.")} className="example-button bg-gray-200 text-blue-500 p-2 rounded mb-2 w-full max-w-md">
              This product was terrible! I am never buying this again.
            </button>
            <button onClick={() => handleExampleClick("This product was great! I loved it and will buy again.")} className="example-button bg-gray-200 text-blue-500 p-2 rounded mb-2 w-full max-w-md">
              This product was great! I loved it and will buy again.
            </button>
          </div>
        </div>
        {rating !== null && <div className="rating-output text-green-500 font-bold mt-6">Rating: {rating}</div>}
        {error && <div className="error-message text-red-500 mt-6">{error}</div>}
      </div>
    </div>
  );
};

export default Home;
