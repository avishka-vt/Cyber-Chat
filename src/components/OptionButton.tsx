import React from 'react';
import type { OptionConfig } from '../config/stateConfigs'; // Fix: Use import type for OptionConfig

// --- Type Definition for Props ---
interface OptionButtonProps {
  option: OptionConfig;
  onClick: (option: OptionConfig) => void;
}

const OptionButton: React.FC<OptionButtonProps> = ({ option, onClick }) => {
  return (
    <button
      onClick={() => onClick(option)}
      className="w-full text-left px-4 py-3 bg-slate-800/60 hover:bg-slate-700/80
                  text-gray-200 rounded-xl border border-slate-600/50
                  hover:border-blue-500/50 transition-all duration-200
                  shadow-lg hover:shadow-blue-500/20 text-sm"
    >
      <span className="font-medium text-blue-400 mr-2">{option.id}.</span>
      {option.text}
    </button>
  );
};

export default OptionButton;