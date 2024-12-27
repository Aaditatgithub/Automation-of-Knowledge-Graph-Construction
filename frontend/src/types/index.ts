// API configuration
export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';export interface SidebarItem {
    title: string;
    path: string;
    icon: React.ComponentType;
  }
  
  export interface Product {
    id: string;
    name: string;
    category: string;
    // Add more fields as needed
  }
  
  export interface Collection {
    id: string;
    name: string;
    count: number;
    // Add more fields as needed
  }