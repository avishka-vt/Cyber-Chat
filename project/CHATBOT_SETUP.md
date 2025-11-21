# Cybersecurity Chatbot - Complete Setup Guide

This document provides complete instructions for setting up and deploying the cybersecurity chatbot backend.

## Overview

The cybersecurity chatbot is a Python Flask backend application that provides AI-powered information about cybersecurity laws, guidelines, and regulations for:
- New York City / United States (NYC)
- Germany
- South Korea

The system uses Google Gemini Pro for AI responses and Supabase for data persistence.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Application                      │
│                   (React / Vue / Angular)                    │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/REST
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Flask Backend API                           │
│                  (Python 3.8+)                              │
│                                                              │
│  ├── Session Management                                     │
│  ├── Conversation Flow                                      │
│  ├── Context Management                                     │
│  └── Out-of-Context Handling                               │
└────────────────┬───────────────┬───────────────────────────┘
                 │               │
    ┌────────────▼──────┐  ┌─────▼──────────────┐
    │ Google Gemini Pro │  │  Supabase Database │
    │   (AI Responses)  │  │  (Data Storage)    │
    └───────────────────┘  └────────────────────┘
```

## Directory Structure

```
project/
├── backend/                          # Python Flask Backend
│   ├── app.py                        # Main Flask application
│   ├── config.py                     # Configuration management
│   ├── database.py                   # Supabase client
│   ├── gemini_service.py             # Google Gemini integration
│   ├── conversation_manager.py       # Session management
│   ├── constants.py                  # Application constants
│   ├── seed_data.py                  # Database seeding
│   ├── run.sh                        # Startup script
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # Environment template
│   ├── README.md                     # Full documentation
│   ├── QUICKSTART.md                 # Quick start guide
│   └── USAGE_EXAMPLES.md             # API examples
│
├── supabase/                         # Supabase Configuration
│   └── migrations/                   # Database migrations
│
└── src/                              # Frontend (React)
    └── (React application files)
```

## Prerequisites

Before starting, ensure you have:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **Google Gemini API Key** (Free)
   - Go to https://ai.google.dev/
   - Click "Get API Key"
   - Create a new API key in Google Cloud Console

3. **Supabase Account**
   - Create account at https://supabase.com
   - Create a new project
   - Get your project URL and API keys

4. **Git** (optional, for cloning)

## Installation Steps

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected packages:
- Flask==3.0.0
- Flask-CORS==4.0.0
- python-dotenv==1.0.0
- google-generativeai==0.3.0
- supabase==2.3.4
- requests==2.31.0

### Step 4: Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000

GEMINI_API_KEY=your_api_key_from_google_ai

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_anon_key_here
SUPABASE_SERVICE_KEY=your_service_role_key_here
```

**Where to find these values:**

- **GEMINI_API_KEY**: From Google AI Studio (https://ai.google.dev/)
- **SUPABASE_URL**: From Supabase Project Settings → API
- **SUPABASE_KEY**: Anon public key from Supabase
- **SUPABASE_SERVICE_KEY**: Service role secret key from Supabase

### Step 5: Set Up Database

#### Option A: Manual SQL Execution (Recommended)

1. Go to Supabase Dashboard
2. Select your project
3. Go to SQL Editor
4. Create new query
5. Copy-paste SQL from `supabase/migrations/001_create_cybersecurity_tables.sql`
6. Execute

OR create the tables manually using the following SQL:

```sql
CREATE TABLE IF NOT EXISTS cybersecurity_laws (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  country_code text NOT NULL,
  title text NOT NULL,
  description text,
  effective_date date,
  source_url text,
  category text,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS cybersecurity_guidelines (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  country_code text NOT NULL,
  name text NOT NULL,
  description text,
  category text,
  source_url text,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS government_portals (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  country_code text NOT NULL,
  portal_name text NOT NULL,
  url text NOT NULL,
  description text,
  category text,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS conversations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id text NOT NULL,
  country_code text NOT NULL,
  user_message text NOT NULL,
  bot_response text NOT NULL,
  created_at timestamptz DEFAULT now()
);

-- Enable RLS
ALTER TABLE cybersecurity_laws ENABLE ROW LEVEL SECURITY;
ALTER TABLE cybersecurity_guidelines ENABLE ROW LEVEL SECURITY;
ALTER TABLE government_portals ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;

-- Create Policies
CREATE POLICY "Anyone can view laws"
  ON cybersecurity_laws FOR SELECT USING (true);

CREATE POLICY "Anyone can view guidelines"
  ON cybersecurity_guidelines FOR SELECT USING (true);

CREATE POLICY "Anyone can view portals"
  ON government_portals FOR SELECT USING (true);

CREATE POLICY "Anyone can insert conversations"
  ON conversations FOR INSERT WITH CHECK (true);

CREATE POLICY "Anyone can view conversations"
  ON conversations FOR SELECT USING (true);

-- Create Indexes
CREATE INDEX idx_cybersecurity_laws_country ON cybersecurity_laws(country_code);
CREATE INDEX idx_cybersecurity_guidelines_country ON cybersecurity_guidelines(country_code);
CREATE INDEX idx_government_portals_country ON government_portals(country_code);
CREATE INDEX idx_conversations_user_id ON conversations(user_id);
CREATE INDEX idx_conversations_country ON conversations(country_code);
```

#### Option B: Automatic Seeding

```bash
python seed_data.py
```

This creates tables and populates placeholder data.

### Step 6: Start the Server

```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Step 7: Verify Installation

In a new terminal:

```bash
# Health check
curl http://localhost:5000/api/health

# List countries
curl http://localhost:5000/api/countries
```

Expected responses:
```json
{"status": "healthy", "service": "cybersecurity_chatbot"}
{"countries": {"NYC": "New York City (USA)", ...}}
```

## Running the Application

### Development Mode

```bash
python app.py
```

### Using the Startup Script

```bash
chmod +x run.sh
./run.sh
```

### Production Mode (using Gunicorn)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Quick Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Check server health |
| `/api/countries` | GET | List available countries |
| `/api/session/create` | POST | Create new chat session |
| `/api/chat` | POST | Send message to chatbot |
| `/api/session/{id}/switch-country` | POST | Change country context |
| `/api/session/{id}/info` | GET | Get session information |
| `/api/session/{id}/end` | POST | End chat session |

## Testing the Chatbot

### Using cURL

```bash
# Create session
curl -X POST http://localhost:5000/api/session/create \
  -H "Content-Type: application/json" \
  -d '{"country_code":"NYC"}'

# Send message (replace SESSION_ID)
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "SESSION_ID",
    "message": "What is the SHIELD Act?"
  }'
```

### Using Python

```python
import requests

client_url = "http://localhost:5000"

# Create session
resp = requests.post(f"{client_url}/api/session/create",
    json={"country_code": "NYC"})
session_id = resp.json()["session_id"]

# Send message
resp = requests.post(f"{client_url}/api/chat",
    json={"session_id": session_id, "message": "What is SHIELD?"})
print(resp.json()["response"])
```

### Using JavaScript/Fetch

```javascript
// Create session
const sessionResp = await fetch('http://localhost:5000/api/session/create', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({country_code: 'NYC'})
});
const {session_id} = await sessionResp.json();

// Send message
const msgResp = await fetch('http://localhost:5000/api/chat', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({session_id, message: "What is GDPR?"})
});
const {response} = await msgResp.json();
console.log(response);
```

## Adding Cybersecurity Data

### Method 1: Update Seed Data

Edit `backend/seed_data.py` and add to:

```python
SEED_LAWS = [
    {
        'country_code': 'NYC',
        'title': 'Your Law Name',
        'description': 'Detailed description here...',
        'category': 'Data Protection',
        'source_url': 'https://example.com',
        'effective_date': '2024-01-01'
    },
    # Add more laws
]

SEED_GUIDELINES = [
    {
        'country_code': 'GERMANY',
        'name': 'Guideline Name',
        'description': 'Description...',
        'category': 'Cybersecurity',
        'source_url': 'https://example.com'
    },
    # Add more guidelines
]

SEED_PORTALS = [
    {
        'country_code': 'SOUTH_KOREA',
        'portal_name': 'Portal Name',
        'url': 'https://example.com',
        'description': 'Description...',
        'category': 'Government Agency'
    },
    # Add more portals
]
```

Then run:
```bash
python seed_data.py
```

### Method 2: Direct Supabase Insert

Via Supabase Dashboard:
1. Go to Table Editor
2. Select the table (cybersecurity_laws, cybersecurity_guidelines, or government_portals)
3. Click "Insert row"
4. Fill in the data
5. Save

### Method 3: API Insert

You can also extend the backend API to support INSERT operations.

## Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution**: Ensure virtual environment is activated and dependencies installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "GEMINI_API_KEY not found"

**Solution**: Check `.env` file has your API key:
```bash
grep GEMINI_API_KEY .env
```

### Issue: "Connection to Supabase failed"

**Solution**: Verify credentials:
```bash
grep SUPABASE .env
```

Ensure URL is correct format: `https://YOUR-PROJECT.supabase.co`

### Issue: "No tables in Supabase"

**Solution**: Execute the SQL migration in Supabase SQL Editor.

### Issue: "Port 5000 already in use"

**Solution**: Change port in `.env`:
```
PORT=5001
```

## Monitoring and Logs

### Enable Debug Logging

Update `.env`:
```
FLASK_DEBUG=True
```

### Check Supabase Logs

In Supabase Dashboard:
1. Go to Logs
2. View database, API, and authentication logs

### Monitor Conversations

```sql
SELECT * FROM conversations ORDER BY created_at DESC LIMIT 10;
```

## Deployment

### Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t chatbot-backend .
docker run -p 5000:5000 --env-file .env chatbot-backend
```

### Cloud Deployment

**Heroku:**
```bash
heroku create your-app-name
git push heroku main
```

**AWS Lambda:**
Use Zappa to deploy Flask to Lambda

**Google Cloud:**
```bash
gcloud app deploy
```

## Performance Optimization

1. **Enable Caching**: Add Redis for conversation caching
2. **Use Connection Pooling**: Configure Supabase connection pool
3. **Rate Limiting**: Implement API rate limiting
4. **Compress Responses**: Enable gzip compression
5. **Database Indexes**: Already configured in migration

## Security Best Practices

1. **Never commit `.env`**: Add to `.gitignore`
2. **Use HTTPS**: Enable SSL in production
3. **Validate Input**: All inputs are validated
4. **CORS Configuration**: Update as needed for production
5. **Rate Limiting**: Implement for public APIs
6. **Logging**: Enable audit logs

## Next Steps

1. **Integrate Frontend**: Connect React app to this backend
2. **Add More Data**: Research and add comprehensive cybersecurity information
3. **Deploy**: Use Docker or cloud platform
4. **Monitor**: Set up error tracking and monitoring
5. **Scale**: Optimize for production traffic

## Support & Resources

- **Backend Documentation**: See `backend/README.md`
- **Quick Start**: See `backend/QUICKSTART.md`
- **API Examples**: See `backend/USAGE_EXAMPLES.md`
- **Google Gemini**: https://ai.google.dev/
- **Supabase Docs**: https://supabase.com/docs
- **Flask Docs**: https://flask.palletsprojects.com/

## File Checklist

After setup, you should have:

- [ ] `.env` file with all credentials
- [ ] Python virtual environment activated
- [ ] All dependencies installed (`pip list`)
- [ ] Supabase tables created
- [ ] Database seeded with placeholder data
- [ ] Flask server running on port 5000
- [ ] API endpoints responding to requests
- [ ] Conversations being saved to database

## Conclusion

Your cybersecurity chatbot backend is now ready! You can:
- Test it with cURL or Postman
- Integrate it with the frontend React app
- Add more researched cybersecurity data
- Deploy it to production

For detailed information, refer to the documentation files in the backend directory.

Happy chatting!
