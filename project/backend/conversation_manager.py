from database import db
from gemini_service import GeminiChatbot
import uuid


class ConversationManager:
    def __init__(self):
        self.chatbots = {}
        self.active_sessions = {}

    def create_session(self, user_id: str = None, country_code: str = 'NYC') -> str:
        """Create a new conversation session"""
        if user_id is None:
            user_id = str(uuid.uuid4())

        session_id = str(uuid.uuid4())

        self.chatbots[session_id] = GeminiChatbot()
        self.active_sessions[session_id] = {
            'user_id': user_id,
            'country_code': country_code,
            'created_at': __import__('datetime').datetime.utcnow()
        }

        return session_id

    def switch_country(self, session_id: str, new_country: str) -> bool:
        """Switch the country context for a session"""
        if session_id in self.active_sessions:
            self.active_sessions[session_id]['country_code'] = new_country
            self.chatbots[session_id].reset_conversation()
            return True
        return False

    def get_country_options(self) -> dict:
        """Return available country options"""
        return {
            'NYC': 'New York City (USA)',
            'GERMANY': 'Germany',
            'SOUTH_KOREA': 'South Korea'
        }

    def handle_user_input(self, session_id: str, user_message: str) -> dict:
        """Process user input and return bot response"""
        if session_id not in self.active_sessions:
            return {'error': 'Invalid session', 'success': False}

        session = self.active_sessions[session_id]
        user_id = session['user_id']
        country_code = session['country_code']

        chatbot = self.chatbots[session_id]

        is_out_of_context, redirect_message = chatbot.handle_out_of_context(user_message, country_code)
        if is_out_of_context:
            db.save_conversation(user_id, country_code, user_message, redirect_message)
            return {
                'response': redirect_message,
                'country': country_code,
                'is_redirect': True,
                'success': True
            }

        laws = db.get_cybersecurity_laws(country_code)
        guidelines = db.get_cybersecurity_guidelines(country_code)

        laws_context = '\n'.join([f"- {law.get('title', 'N/A')}: {law.get('description', 'N/A')}" for law in laws]) if laws else ""
        guidelines_context = '\n'.join([f"- {gl.get('name', 'N/A')}: {gl.get('description', 'N/A')}" for gl in guidelines]) if guidelines else ""

        bot_response = chatbot.get_response(user_message, country_code, laws_context, guidelines_context)

        db.save_conversation(user_id, country_code, user_message, bot_response)

        return {
            'response': bot_response,
            'country': country_code,
            'is_redirect': False,
            'success': True
        }

    def get_session_info(self, session_id: str) -> dict:
        """Get information about a session"""
        if session_id not in self.active_sessions:
            return {'error': 'Invalid session'}

        session = self.active_sessions[session_id]
        return {
            'user_id': session['user_id'],
            'country_code': session['country_code'],
            'created_at': session['created_at'].isoformat()
        }

    def end_session(self, session_id: str) -> bool:
        """End a conversation session"""
        if session_id in self.chatbots:
            del self.chatbots[session_id]
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
        return True


conversation_manager = ConversationManager()
