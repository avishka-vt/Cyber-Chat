import React from 'react';
import { Shield } from 'lucide-react';

// Define the component as a Functional Component (FC)
const Header: React.FC = () => {
  return (
    <div className="bg-slate-800/90 backdrop-blur-sm border-b border-blue-500/30 shadow-lg">
      <div className="max-w-6xl mx-auto px-6 py-4">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-blue-500/20 rounded-lg">
            <Shield className="w-8 h-8 text-blue-400" />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-white">Cybersecurity Information Portal</h1>
            <p className="text-sm text-blue-300">Global Cyber Laws & Regulatory Guidance</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;