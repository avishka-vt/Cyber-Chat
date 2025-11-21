"""
Constants for the cybersecurity chatbot application
"""

COUNTRIES = {
    'NYC': {
        'name': 'New York City (USA)',
        'full_name': 'New York City / United States',
        'region': 'North America',
        'timezone': 'EST'
    },
    'GERMANY': {
        'name': 'Germany',
        'full_name': 'Federal Republic of Germany',
        'region': 'Europe',
        'timezone': 'CET'
    },
    'SOUTH_KOREA': {
        'name': 'South Korea',
        'full_name': 'Republic of Korea',
        'region': 'Asia',
        'timezone': 'KST'
    }
}

OUT_OF_CONTEXT_KEYWORDS = [
    'weather', 'sports', 'entertainment', 'movies', 'games', 'cooking',
    'jokes', 'music', 'celebrities', 'politics', 'religion', 'philosophy',
    'recipe', 'fashion', 'travel', 'history', 'science', 'math',
    'cooking', 'art', 'literature', 'jokes', 'memes', 'funny'
]

CYBERSECURITY_KEYWORDS = [
    'cybersecurity', 'security', 'compliance', 'law', 'regulation', 'gdpr',
    'shield', 'hipaa', 'pipa', 'data protection', 'privacy', 'breach',
    'encryption', 'authentication', 'access control', 'incident', 'audit',
    'vulnerability', 'risk', 'threat', 'protection', 'defense', 'secure',
    'certificate', 'ssl', 'firewall', 'network', 'infrastructure',
    'policy', 'requirement', 'standard', 'guideline', 'framework',
    'bsi', 'kisa', 'ftc', 'fda', 'sec', 'critical infrastructure'
]

SYSTEM_PROMPTS = {
    'NYC': """You are an expert cybersecurity compliance advisor specializing in New York City and United States cybersecurity laws and regulations.

Your expertise includes:
- New York SHIELD Act
- HIPAA (healthcare data protection)
- FTC Guidelines and enforcement
- Sector-specific requirements
- Federal cybersecurity standards

Your role is to:
1. Provide accurate information about US and NYC cybersecurity laws
2. Explain compliance requirements clearly with specific examples
3. Answer questions about data protection and privacy standards
4. Direct users to relevant government portals and resources
5. Provide actionable compliance advice

Always be professional, cite specific laws, and acknowledge when information needs updating.""",

    'GERMANY': """You are an expert cybersecurity compliance advisor specializing in German and European cybersecurity laws and regulations.

Your expertise includes:
- GDPR (General Data Protection Regulation)
- German IT Security Act (BSI)
- NIS Directive implementation
- German data protection standards
- European cybersecurity framework

Your role is to:
1. Provide accurate information about German and EU cybersecurity laws
2. Explain GDPR requirements with practical examples
3. Answer questions about critical infrastructure protection
4. Direct users to BSI, BfDI, and EU resources
5. Provide compliance guidance for German businesses

Always be thorough, cite specific regulations, and provide EU-wide context.""",

    'SOUTH_KOREA': """You are an expert cybersecurity compliance advisor specializing in South Korean cybersecurity laws and regulations.

Your expertise includes:
- PIPA (Personal Information Protection Act)
- ICN Act (Information and Communications Network Act)
- KISA guidelines and standards
- Critical infrastructure protection
- Korean data protection framework

Your role is to:
1. Provide accurate information about South Korean cybersecurity laws
2. Explain PIPA requirements and personal information handling
3. Answer questions about Korean compliance standards
4. Direct users to KISA and government resources
5. Provide guidance for businesses operating in South Korea

Always be precise, cite Korean laws, and provide practical guidance."""
}

ERROR_MESSAGES = {
    'invalid_session': 'The session ID is invalid or has expired. Please create a new session.',
    'invalid_country': 'Invalid country code. Supported countries: NYC, GERMANY, SOUTH_KOREA',
    'empty_message': 'Please provide a non-empty message.',
    'api_error': 'An error occurred while processing your request. Please try again.',
    'database_error': 'Unable to retrieve data from the database. Please try again.',
    'ai_error': 'Unable to generate a response. Please try again.'
}

SUCCESS_MESSAGES = {
    'session_created': 'Session created successfully',
    'country_switched': 'Country context switched successfully',
    'session_ended': 'Session ended successfully'
}

REDIRECT_MESSAGES = {
    'NYC': "I appreciate your question, but I specialize in cybersecurity compliance topics for New York City and the USA. Let's refocus on your cybersecurity concerns. Could you tell me about specific compliance or security topics you'd like to discuss?",
    'GERMANY': "I appreciate your question, but I specialize in cybersecurity compliance topics for Germany and Europe. Let's refocus on your cybersecurity concerns. Could you tell me about specific compliance or security topics you'd like to discuss?",
    'SOUTH_KOREA': "I appreciate your question, but I specialize in cybersecurity compliance topics for South Korea. Let's refocus on your cybersecurity concerns. Could you tell me about specific compliance or security topics you'd like to discuss?"
}

MAX_CONVERSATION_HISTORY = 50
CONVERSATION_TIMEOUT_MINUTES = 30
MAX_MESSAGE_LENGTH = 5000
MIN_MESSAGE_LENGTH = 1

API_RESPONSE_CODES = {
    'success': 200,
    'created': 201,
    'bad_request': 400,
    'unauthorized': 401,
    'forbidden': 403,
    'not_found': 404,
    'conflict': 409,
    'server_error': 500
}

RATE_LIMIT = {
    'enabled': False,
    'requests_per_minute': 60,
    'requests_per_hour': 1000
}

LOGGING = {
    'level': 'INFO',
    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
}

DATABASE_INDEXES = {
    'cybersecurity_laws': ['country_code', 'category', 'created_at'],
    'cybersecurity_guidelines': ['country_code', 'category'],
    'government_portals': ['country_code', 'category'],
    'conversations': ['user_id', 'country_code', 'created_at']
}

GEMINI_MODEL_CONFIG = {
    'model': 'gemini-pro',
    'temperature': 0.7,
    'top_p': 0.95,
    'top_k': 40,
    'max_output_tokens': 1000
}
