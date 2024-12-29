// import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Sidebar } from './components/layout/Sidebar';
import  {ProductCatalogue}  from './components/pages/ProductCatalogue';
import  {KnowledgeGraphs}  from './components/pages/KnowledgeGraphs';
// Import other pages as needed

function App() {
  return (
    <Router>
      <div className="flex min-h-screen bg-gray-100">
        <Sidebar />
        <main className="flex-1 ml-64 p-4">
          <Routes>
            <Route path="/products" element={<ProductCatalogue />} />
            <Route path="/graphs" element={<KnowledgeGraphs />} />
            {/* Add other routes */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
