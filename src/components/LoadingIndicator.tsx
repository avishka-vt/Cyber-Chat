import React from 'react';
import { Bot } from 'lucide-react';

const LoadingIndicator: React.FC = () => {
  return (
    <div className="flex justify-start">
      <div className="flex gap-3 max-w-3xl">
        <div className="flex-shrink-0 w-10 h-10 rounded-full bg-slate-700 flex items-center justify-center">
          <Bot className="w-5 h-5 text-blue-400" />
        </div>
        <div className="bg-slate-800/80 rounded-2xl px-5 py-3 border border-slate-700">
          <div className="flex gap-2">
            <div className="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
            <div className="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
            <div className="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoadingIndicator;