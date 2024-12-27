import React from 'react';
import { Network } from 'lucide-react';

export function KnowledgeGraphs() {
  return (
    <div className="p-6">
      <div className="flex items-center gap-3 mb-6">
        <Network className="w-6 h-6 text-blue-500" />
        <h1 className="text-2xl font-bold">Knowledge Graphs</h1>
      </div>
      
      <div className="bg-white p-6 rounded-lg shadow">
        <p className="text-gray-600">Knowledge graph visualization will be implemented here.</p>
      </div>
    </div>
  );
}