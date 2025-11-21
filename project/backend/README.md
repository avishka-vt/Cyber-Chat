# Cybersecurity Chatbot Backend

A Python Flask backend for a cybersecurity compliance chatbot powered by Google Gemini Pro AI. The chatbot provides information on cybersecurity laws, guidelines, and regulations for NYC, Germany, and South Korea.

## Features

- **Multi-country Support**: Provides cybersecurity information for NYC (USA), Germany, and South Korea
- **AI-Powered Conversations**: Uses Google Gemini Pro for intelligent responses
- **Context Management**: Maintains conversation history and context
- **Out-of-Context Handling**: Gracefully redirects off-topic questions back to cybersecurity
- **Database Integration**: Stores laws, guidelines, portals, and conversation history in Supabase
- **RESTful API**: Complete API for chatbot interactions
- **CORS Enabled**: Ready for integration with frontend applications

## Setup

### Prerequisites

- Python 3.8+
- Google Gemini API key
- Supabase project and credentials

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Update `.env` with your credentials:
```
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000

GEMINI_API_KEY=your_gemini_api_key_here

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_SERVICE_KEY=your_supabase_service_role_key
```

### Database Setup

1. Create tables in Supabase using the provided SQL migration script (`supabase/migrations/001_create_cybersecurity_tables.sql`)

2. Seed the database with initial data:
```bash
python seed_data.py
```

This will populate placeholder data for:
- Cybersecurity laws
- Guidelines and best practices
- Government portals and resources

## Running the Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### 1. Health Check
```
GET /api/health
```
Returns server status.

### 2. Get Available Countries
```
GET /api/countries
```
Returns list of available countries and their codes.

### 3. Create Session
```
POST /api/session/create
Content-Type: application/json

{
  "user_id": "optional_user_id",
  "country_code": "NYC"  // NYC, GERMANY, or SOUTH_KOREA
}
```
Creates a new conversation session and returns a session ID.

### 4. Send Chat Message
```
POST /api/chat
Content-Type: application/json

{
  "session_id": "session_id_from_create",
  "message": "What are the cybersecurity requirements for businesses in NYC?"
}
```
Sends a message and receives AI-powered response.

### 5. Switch Country
```
POST /api/session/{session_id}/switch-country
Content-Type: application/json

{
  "country_code": "GERMANY"
}
```
Changes the country context for an ongoing conversation.

### 6. Get Session Info
```
GET /api/session/{session_id}/info
```
Returns information about an active session.

### 7. End Session
```
POST /api/session/{session_id}/end
```
Terminates a session.

## Project Structure

```
backend/
├── app.py                    # Flask application and API endpoints
├── config.py                 # Configuration management
├── database.py               # Supabase database client
├── gemini_service.py         # Gemini Pro AI integration
├── conversation_manager.py   # Session and conversation management
├── seed_data.py              # Database seeding script
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## Supported Countries and Topics

### NYC (New York/United States)
- SHIELD Act and data protection laws
- HIPAA regulations for healthcare
- FTC guidelines
- Sector-specific requirements

### Germany
- GDPR compliance
- BSI IT Security Act
- Cloud security standards
- Critical infrastructure protection

### South Korea
- PIPA (Personal Information Protection Act)
- ICN Act (Information and Communications Network Act)
- KISA guidelines
- Critical infrastructure protection

## Adding More Research Data

The system is designed to be easily extensible. To add more comprehensive cybersecurity information:

1. **Update Laws**: Modify the `SEED_LAWS` dictionary in `seed_data.py`
2. **Update Guidelines**: Modify the `SEED_GUIDELINES` dictionary
3. **Update Portals**: Modify the `SEED_PORTALS` dictionary
4. **Add Directly via Supabase**: Use Supabase dashboard to insert data into the respective tables

Each record can include:
- Title/Name
- Detailed description
- Category
- Source URL/Link
- Effective date (for laws)

## Conversation Flow

The chatbot follows a structured flow:

1. User initiates a session with a country selection
2. Chatbot greets the user and asks what cybersecurity topic they need help with
3. User sends a message
4. System checks if the message is out of context
5. If out of context, bot gracefully redirects to cybersecurity topics
6. If relevant, bot retrieves relevant laws and guidelines from the database
7. Gemini Pro generates a contextual response
8. Conversation is saved to the database for analysis
9. Response is returned to the user

## Error Handling

The system gracefully handles:
- Invalid session IDs
- Missing or malformed requests
- API failures (with fallback messages)
- Out-of-context questions
- Database connection issues

## Performance Considerations

- Conversations are indexed by user_id and country_code for fast retrieval
- Laws and guidelines are indexed by country for quick filtering
- Supabase RLS policies ensure data is publicly readable while maintaining security
- Session state is maintained in memory for immediate access

## Future Enhancements

- Multi-language support
- Advanced context awareness with RAG (Retrieval-Augmented Generation)
- Analytics dashboard for conversation insights
- Integration with official cybersecurity APIs
- Document upload and analysis
- Compliance checklist generation
- Real-time regulatory updates

## Troubleshooting

### "GEMINI_API_KEY not found"
Ensure the API key is added to your `.env` file.

### "Connection to Supabase failed"
Check your Supabase URL and credentials in `.env`.

### "Database tables don't exist"
Run the SQL migration script in Supabase or execute `seed_data.py` after creating tables.

### "No laws/guidelines found"
Ensure the database has been seeded with data via `seed_data.py`.

## Support

For issues or questions, refer to:
- [Google Gemini API Documentation](https://ai.google.dev/)
- [Supabase Documentation](https://supabase.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
