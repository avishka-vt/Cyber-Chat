import google.generativeai as genai
from config import config

genai.configure(api_key=config.GEMINI_API_KEY)


class GeminiChatbot:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.conversation_history = []

    def create_system_prompt(self, country_code: str, laws_context: str, guidelines_context: str) -> str:
        country_names = {
            'NYC': 'New York City/United States',
            'GERMANY': 'Germany',
            'SOUTH_KOREA': 'South Korea'
        }

        country_name = country_names.get(country_code, country_code)

        system_prompt = f"""You are an expert cybersecurity compliance advisor specializing in {country_name}'s cybersecurity laws and regulations.

Your role is to:
1. Provide accurate information about cybersecurity laws, regulations, and guidelines in {country_name}
2. Explain compliance requirements clearly
3. Answer questions about data protection, privacy, and security standards
4. Direct users to relevant government portals and official resources

Context about {country_name}:
Laws and Regulations:
{laws_context if laws_context else "Information will be added as research progresses."}

Guidelines:
{guidelines_context if guidelines_context else "Guidelines will be added as research progresses."}

Important Instructions:
- Stay focused on cybersecurity compliance topics
- If asked about unrelated topics, politely redirect to cybersecurity matters
- Always cite the specific law or regulation when providing compliance information
- Be professional and clear in your explanations
- If you don't have specific information, acknowledge it and suggest consulting official sources
- Provide actionable advice where appropriate

Start by greeting the user and asking what specific cybersecurity compliance topic they'd like to explore."""

        return system_prompt

    def get_response(self, user_message: str, country_code: str, laws_context: str = "", guidelines_context: str = "") -> str:
        try:
            system_prompt = self.create_system_prompt(country_code, laws_context, guidelines_context)

            self.conversation_history.append({
                "role": "user",
                "parts": [user_message]
            })

            chat = self.model.start_chat(history=self.conversation_history)

            response = chat.send_message(system_prompt + "\n\nUser: " + user_message)

            bot_response = response.text

            self.conversation_history.append({
                "role": "model",
                "parts": [bot_response]
            })

            return bot_response

        except Exception as e:
            error_message = f"Error generating response: {str(e)}"
            print(error_message)
            return "I apologize, but I encountered an error processing your request. Please try again."

    def reset_conversation(self):
        self.conversation_history = []

    def handle_out_of_context(self, user_message: str, country_code: str) -> tuple[bool, str]:
        """
        Checks if the message is out of context and returns a redirection message.
        Returns (is_out_of_context, response)
        """
        out_of_context_keywords = [
            'weather', 'sports', 'entertainment', 'movies', 'games', 'cooking',
            'jokes', 'music', 'celebrities', 'politics', 'religion'
        ]

        message_lower = user_message.lower()

        for keyword in out_of_context_keywords:
            if keyword in message_lower:
                redirect_response = f"I appreciate your question, but I specialize in cybersecurity compliance topics for {country_code}. Let's refocus on your cybersecurity concerns. Could you tell me about specific compliance or security topics you'd like to discuss?"
                return True, redirect_response

        return False, ""
