import type { ChatState } from '../utils/constants';

// --- Type Definitions for API Communication ---

/** Defines the structure of the data sent to the backend chat endpoint. */
export interface ChatRequest {
  query: string;
  state: ChatState;
  selectedOptionId?: number; // Optional for menu selections
}

/** Defines the structure of the data received from the backend. */
export interface ChatResponse {
  type: 'text' | 'menu';
  message: string;
  newState: ChatState;
  options?: OptionConfig[]; // Present if type is 'menu'
  isInputRequired: boolean;
}

// Re-exporting the OptionConfig type from stateConfigs.ts for use here
export interface OptionConfig {
  id: number;
  text: string;
  nextState: ChatState;
}

// --- API Implementation ---

export const chatAPI = {
  sendQuery: async (request: ChatRequest): Promise<ChatResponse> => {
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        // Attempt to parse error message if available, otherwise use status text
        const errorText = await response.text();
        throw new Error(`HTTP error! Status: ${response.status}. Details: ${errorText}`);
      }

      const data: ChatResponse = await response.json();
      return data;
    } catch (error) {
      console.error('API Error:', error);
      // Re-throw to allow the calling component to handle the error state
      throw new Error(error instanceof Error ? error.message : 'An unknown API error occurred');
    }
  },
};