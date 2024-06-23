import React from 'react';
import Search from '../components/Search';

const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="bg-white shadow-md rounded-lg p-8 w-full max-w-2xl">
        <h1 className="text-4xl font-bold text-gray-900 mb-4 text-center">Welcome to my Weaviate Sample Project</h1>
        <p className="text-gray-700 mb-8 text-center">Enter a rating below to get the model's predicted rating (1-5).</p>
        <Search />
      </div>
    </div>
  );
};

export default Home;
