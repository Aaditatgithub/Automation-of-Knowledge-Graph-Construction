import React, { useState } from 'react';
import { Search } from 'lucide-react';

export function ProductSearch() {
  const [searchQuery, setSearchQuery] = useState('');

  return (
    <div className="p-6">
      <div className="flex items-center gap-3 mb-6">
        <Search className="w-6 h-6 text-blue-500" />
        <h1 className="text-2xl font-bold">Product Search</h1>
      </div>
      
      <div className="max-w-2xl">
        <div className="relative">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search for products..."
            className="w-full px-4 py-3 pl-12 bg-white border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <Search className="w-5 h-5 text-gray-400 absolute left-4 top-1/2 transform -translate-y-1/2" />
        </div>
        
        <div className="mt-6">
          {/* Search results will be displayed here */}
          <p className="text-gray-600">Enter a search term to find products</p>
        </div>
      </div>
    </div>
  );
}