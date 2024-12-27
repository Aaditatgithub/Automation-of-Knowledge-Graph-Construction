import React from 'react';
import { LayoutDashboard, Database, Network, TrendingUp, Search } from 'lucide-react';
import { SidebarItem } from '../../types';

const sidebarItems: SidebarItem[] = [
  {
    title: 'Products Catalogue',
    path: '/products',
    icon: Database,
  },
  {
    title: 'Knowledge Graphs',
    path: '/graphs',
    icon: Network,
  },
  {
    title: 'Trend Analytics',
    path: '/trends',
    icon: TrendingUp,
  },
  {
    title: 'Product Search',
    path: '/search',
    icon: Search,
  },
];

export function Sidebar() {
  return (
    <div className="h-screen w-64 bg-gray-900 text-white p-4 fixed left-0 top-0">
      <div className="flex items-center gap-2 mb-8">
        <LayoutDashboard className="w-8 h-8 text-blue-400" />
        <h1 className="text-xl font-bold">EstiloViento</h1>
      </div>
      
      <nav>
        {sidebarItems.map((item) => (
          <button
            key={item.path}
            className="w-full flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-lg transition-colors mb-1"
            onClick={() => console.log(`Navigate to ${item.path}`)}
          >
            <item.icon className="w-5 h-5" />
            <span>{item.title}</span>
          </button>
        ))}
      </nav>
    </div>
  );
}