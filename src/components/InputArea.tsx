// ============================================
// Front/src/components/InputArea.tsx
// ============================================

import React from 'react';
import { Send } from 'lucide-react';

// --- Type Definition for Props ---
interface InputAreaProps {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
  isLoading: boolean;
}

const InputArea: React.FC<InputAreaProps> = ({ value, onChange, onSend, isLoading }) => {
  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  return (
    <div className="bg-slate-800/90 backdrop-blur-sm border-t border-blue-500/30 px-4 py-4">
      <div className="max-w-4xl mx-auto">
        <div className="flex gap-3 items-end">
          <div className="flex-1 bg-slate-900/50 rounded-2xl border border-slate-700 focus-within:border-blue-500 transition-colors">
            <textarea
              value={value}
              onChange={(e) => onChange(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your cybersecurity question here..."
              className="w-full bg-transparent text-gray-100 px-5 py-4 resize-none focus:outline-none placeholder-gray-500 text-sm"
              rows={3}
            />
          </div>
          <button
            onClick={onSend}
            // Check if value is empty/whitespace OR if loading is true
            disabled={!value.trim() || isLoading}
            className="px-6 py-4 bg-blue-500 hover:bg-blue-600 disabled:bg-slate-700
                      disabled:cursor-not-allowed text-white rounded-2xl transition-colors
                      shadow-lg hover:shadow-blue-500/50 disabled:shadow-none"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default InputArea;