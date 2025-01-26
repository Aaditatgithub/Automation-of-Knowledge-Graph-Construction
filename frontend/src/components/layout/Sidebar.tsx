import { useNavigate } from 'react-router-dom';
import { LayoutDashboard, Database, Network } from 'lucide-react';
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
  // Add other items as needed
];

export function Sidebar() {
  const navigate = useNavigate();

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
            onClick={() => navigate(item.path)}
          >
            <item.icon className="w-5 h-5" />
            <span>{item.title}</span>
          </button>
        ))}
      </nav>
    </div>
  );
}
