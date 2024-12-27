import React from 'react';
import { Sidebar } from './components/layout/Sidebar';
import { ProductCatalogue } from './components/pages/ProductCatalogue';
import { KnowledgeGraphs } from './components/pages/KnowledgeGraphs';
import { TrendAnalytics } from './components/pages/TrendAnalytics';
import { ProductSearch } from './components/pages/ProductSearch';

function App() {
  return (
    <div className="flex min-h-screen bg-gray-100">
      <Sidebar />
      <main className="flex-1 ml-64 p-4">
        <ProductCatalogue />
        {/* Other components will be rendered based on navigation */}
      </main>
    </div>
  );
}

export default App;