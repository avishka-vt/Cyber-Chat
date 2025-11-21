# Quick Start Guide

Get the cybersecurity chatbot running in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free at https://ai.google.dev/)
- Supabase account and credentials

## Step 1: Clone and Navigate

```bash
cd backend
```

## Step 2: Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```
GEMINI_API_KEY=your_api_key_from_google_ai
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_anon_key
SUPABASE_SERVICE_KEY=your_service_role_key
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Set Up Database

### Option A: Using the SQL Script

1. Go to your Supabase project dashboard
2. Open the SQL Editor
3. Create a new query
4. Copy and paste the contents from `supabase/migrations/001_create_cybersecurity_tables.sql`
5. Run the query

### Option B: Auto-seeding

```bash
python seed_data.py
```

This will create tables and populate placeholder data.

## Step 5: Run the Server

```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

## Step 6: Test the API

Open a new terminal and run:

```bash
# Health check
curl http://localhost:5000/api/health

# Create a session
curl -X POST http://localhost:5000/api/session/create \
  -H "Content-Type: application/json" \
  -d '{"country_code":"NYC"}'
```

## Step 7: Chat with the Bot

Using the session ID from the previous response:

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "YOUR_SESSION_ID_HERE",
    "message": "What is the SHIELD Act?"
  }'
```

## Common Issues

### "No module named 'google'"
```bash
pip install google-generativeai
```

### "No module named 'supabase'"
```bash
pip install supabase
```

### "Connection refused"
Make sure the Flask server is running on port 5000.

### "Supabase connection failed"
Check your `.env` credentials are correct.

## Next Steps

1. **Integrate with Frontend**: See the React app in `../src`
2. **Add More Data**: Update `seed_data.py` with research data
3. **Deploy**: Use Docker or cloud platform (Heroku, AWS, etc.)
4. **Monitor**: Check `conversations` table for usage patterns

## API Quick Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Check server status |
| `/api/countries` | GET | List available countries |
| `/api/session/create` | POST | Start new session |
| `/api/chat` | POST | Send message and get response |
| `/api/session/{id}/switch-country` | POST | Change country context |
| `/api/session/{id}/info` | GET | Get session details |
| `/api/session/{id}/end` | POST | End session |

## Python Quick Test

Create `test_chat.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000"

# Create session
session_response = requests.post(
    f"{BASE_URL}/api/session/create",
    json={"country_code": "NYC"}
)
session_id = session_response.json()["session_id"]
print(f"Session created: {session_id}\n")

# Ask questions
questions = [
    "What is the SHIELD Act?",
    "Who needs to comply?",
    "What are the penalties?"
]

for question in questions:
    response = requests.post(
        f"{BASE_URL}/api/chat",
        json={"session_id": session_id, "message": question}
    )
    data = response.json()
    print(f"Q: {question}")
    print(f"A: {data['response']}\n")

# End session
requests.post(f"{BASE_URL}/api/session/{session_id}/end")
print("Session ended")
```

Run it:
```bash
python test_chat.py
```

## Database Schema

After setup, you'll have these tables:

- `cybersecurity_laws`: Laws and regulations
- `cybersecurity_guidelines`: Best practices and guidelines
- `government_portals`: Official resources
- `conversations`: Chat history for analysis

## Adding More Data

Edit `seed_data.py` and add your researched information to:
- `SEED_LAWS`
- `SEED_GUIDELINES`
- `SEED_PORTALS`

Then run:
```bash
python seed_data.py
```

Or add directly via Supabase dashboard.

## File Structure

```
backend/
├── app.py                 # Main Flask app
├── config.py              # Configuration
├── database.py            # Supabase client
├── gemini_service.py      # AI integration
├── conversation_manager.py # Session management
├── seed_data.py           # Database seeding
├── requirements.txt       # Dependencies
├── .env.example           # Environment template
├── README.md              # Full documentation
├── QUICKSTART.md          # This file
└── USAGE_EXAMPLES.md      # API examples
```

## Production Deployment

For production use:

1. Set `FLASK_DEBUG=False` in `.env`
2. Use a production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
3. Set up environment variables securely
4. Use a production database
5. Enable HTTPS/SSL
6. Set up monitoring and logging

## Support

For detailed information, see:
- `README.md` - Full documentation
- `USAGE_EXAMPLES.md` - API usage examples

Happy chatting!
