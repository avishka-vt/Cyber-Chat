import React from 'react';
import { MessageCircle, Bot } from 'lucide-react';
import type { MessageType } from '../utils/constants'; // Fix: Use import type for MessageType

// --- Type Definition for Props ---
interface Message {
  text: string;
  type: MessageType; // 'user' or 'bot'
  id: number;
}

interface MessageBubbleProps {
  message: Message;
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const isUser = message.type === 'user';
  
  // Replace markdown-style bolding (**) with simple HTML tags for display
  const formattedText = message.text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={`flex gap-3 max-w-3xl ${isUser ? 'flex-row-reverse' : ''}`}>
        <div className={`flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center ${
          isUser ? 'bg-blue-500' : 'bg-slate-700'
        }`}>
          {isUser ? (
            <MessageCircle className="w-5 h-5 text-white" />
          ) : (
            <Bot className="w-5 h-5 text-blue-400" />
          )}
        </div>
        <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'}`}>
          <div className={`rounded-2xl px-5 py-3 ${
            isUser               
              ? 'bg-blue-500 text-white' 
              : 'bg-slate-800/80 text-gray-100 border border-slate-700'
          }`}>
            {/* We use dangerouslySetInnerHTML to render simple markdown bolding */}
            <p 
              className="whitespace-pre-line text-sm leading-relaxed"
              dangerouslySetInnerHTML={{ __html: formattedText }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default MessageBubble;