from supabase import create_client
from config import config


class SupabaseDB:
    def __init__(self):
        self.client = create_client(config.SUPABASE_URL, config.SUPABASE_SERVICE_KEY)

    def get_cybersecurity_laws(self, country_code: str):
        try:
            response = self.client.table('cybersecurity_laws').select('*').eq('country_code', country_code).execute()
            return response.data
        except Exception as e:
            print(f"Error fetching laws: {e}")
            return []

    def get_guidelines(self, country_code: str):
        try:
            response = self.client.table('cybersecurity_guidelines').select('*').eq('country_code', country_code).execute()
            return response.data
        except Exception as e:
            print(f"Error fetching guidelines: {e}")
            return []

    def get_portals(self, country_code: str):
        try:
            response = self.client.table('government_portals').select('*').eq('country_code', country_code).execute()
            return response.data
        except Exception as e:
            print(f"Error fetching portals: {e}")
            return []

    def save_conversation(self, user_id: str, country_code: str, user_message: str, bot_response: str):
        try:
            self.client.table('conversations').insert({
                'user_id': user_id,
                'country_code': country_code,
                'user_message': user_message,
                'bot_response': bot_response
            }).execute()
        except Exception as e:
            print(f"Error saving conversation: {e}")

    def get_conversation_history(self, user_id: str, limit: int = 10):
        try:
            response = self.client.table('conversations').select('*').eq('user_id', user_id).order('created_at', desc=True).limit(limit).execute()
            return response.data[::-1]
        except Exception as e:
            print(f"Error fetching conversation history: {e}")
            return []


db = SupabaseDB()
