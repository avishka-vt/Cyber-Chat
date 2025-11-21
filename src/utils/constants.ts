export const API_BASE_URL = '/api';

export const API_ENDPOINTS = {
  CHAT: `${API_BASE_URL}/chat`,
} as const;

export const MESSAGE_TYPES = {
  USER: 'user',
  BOT: 'bot',
} as const;

export const STATES = {
  MAIN_MENU: 'S_0',
  COUNTRY_SELECTION: 'S_1',
  AI_QUERY: 'S_2',
  OOC_HANDLER: 'S_3',
  EXIT: 'EXIT',
} as const;

// Helper Types derived from the constants
export type MessageType = typeof MESSAGE_TYPES[keyof typeof MESSAGE_TYPES];
export type ChatState = typeof STATES[keyof typeof STATES] | string; // string is needed for the specific country sub-states