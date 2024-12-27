import React from 'react';
import { TrendingUp } from 'lucide-react';

export function TrendAnalytics() {
  return (
    <div className="p-6">
      <div className="flex items-center gap-3 mb-6">
        <TrendingUp className="w-6 h-6 text-blue-500" />
        <h1 className="text-2xl font-bold">Trend Analytics</h1>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="font-semibold mb-4">Customer Sentiment</h3>
          <div className="h-64 bg-gray-100 rounded flex items-center justify-center">
            Sentiment Analysis Chart
          </div>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="font-semibold mb-4">Trend Forecast</h3>
          <div className="h-64 bg-gray-100 rounded flex items-center justify-center">
            Trend Forecast Chart
          </div>
        </div>
      </div>
    </div>
  );
}