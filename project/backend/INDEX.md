# Cybersecurity Chatbot Backend - File Index

Complete guide to all backend files and their purposes.

## Quick Start Files

### 📖 Documentation
| File | Purpose |
|------|---------|
| `README.md` | Full backend documentation with features and setup |
| `QUICKSTART.md` | 5-minute quick start guide |
| `USAGE_EXAMPLES.md` | API usage examples (cURL, Python, JavaScript) |
| `INDEX.md` | This file - complete file reference |

### ⚙️ Configuration
| File | Purpose |
|------|---------|
| `.env.example` | Environment variables template |
| `requirements.txt` | Python package dependencies |

### 🚀 Startup
| File | Purpose |
|------|---------|
| `run.sh` | Bash startup script for Unix/Linux/Mac |

## Core Application Files

### 🎯 Main Application
**File:** `app.py`
- Flask application entry point
- Defines all REST API endpoints
- Sets up CORS headers
- Error handling and status codes
- Main server initialization

**Key Endpoints:**
- GET `/api/health` - Server health check
- GET `/api/countries` - List available countries
- POST `/api/session/create` - Create new chat session
- POST `/api/chat` - Send message to chatbot
- POST `/api/session/{id}/switch-country` - Change country
- GET `/api/session/{id}/info` - Get session info
- POST `/api/session/{id}/end` - End session

### ⚙️ Configuration Management
**File:** `config.py`
- Loads environment variables from `.env`
- Centralizes configuration
- Provides single source of truth for app settings

### 💾 Database Layer
**File:** `database.py`
- Supabase database client initialization
- Methods to retrieve cybersecurity laws
- Methods to retrieve guidelines
- Methods to retrieve government portals
- Methods to save conversations
- Methods to retrieve conversation history

**Key Methods:**
- `get_cybersecurity_laws(country_code)` - Fetch laws for country
- `get_guidelines(country_code)` - Fetch guidelines
- `get_portals(country_code)` - Fetch government portals
- `save_conversation()` - Save chat to database
- `get_conversation_history()` - Retrieve past conversations

### 🤖 AI Integration
**File:** `gemini_service.py`
- Google Gemini Pro API integration
- Conversation history management
- System prompt generation per country
- Out-of-context detection and redirection
- Response generation with context awareness

**Key Methods:**
- `create_system_prompt()` - Generate country-specific AI instructions
- `get_response()` - Get AI-generated response
- `reset_conversation()` - Clear conversation history
- `handle_out_of_context()` - Detect off-topic questions

### 🔄 Session Management
**File:** `conversation_manager.py`
- Session creation and management
- Country context switching
- User input processing
- Conversation flow coordination
- Session information retrieval

**Key Methods:**
- `create_session()` - Start new conversation
- `switch_country()` - Change country context
- `handle_user_input()` - Process user message
- `get_session_info()` - Get session details
- `end_session()` - Terminate session

### 📊 Constants and Configuration
**File:** `constants.py`
- Country definitions and metadata
- Out-of-context keywords
- Cybersecurity keywords
- System prompts for each country
- Error messages
- Success messages
- Redirect messages
- API response codes
- Rate limiting configuration
- Logging configuration
- Database index definitions
- Gemini model configuration

## Data and Seeding

### 🌱 Database Seeding
**File:** `seed_data.py`
- Placeholder data for cybersecurity laws
- Placeholder data for guidelines
- Placeholder data for government portals
- Database population function
- Can be modified to add researched data

**Data Structure:**

```
SEED_LAWS:
  - NYC: SHIELD Act, HIPAA
  - GERMANY: GDPR, BSI IT Security Act
  - SOUTH_KOREA: PIPA, ICN Act

SEED_GUIDELINES:
  - NYC: NIST Framework, CIS Controls
  - GERMANY: C5 Audit, BSI Baseline
  - SOUTH_KOREA: KISA Guidelines, Critical Infrastructure

SEED_PORTALS:
  - NYC: NY State, FTC
  - GERMANY: BSI, BfDI
  - SOUTH_KOREA: KISA, PIPC
```

## Database Structure

### Tables Created

1. **cybersecurity_laws**
   - Stores cybersecurity laws and regulations
   - Fields: id, country_code, title, description, effective_date, source_url, category, created_at, updated_at
   - Indexed by: country_code

2. **cybersecurity_guidelines**
   - Stores best practices and guidelines
   - Fields: id, country_code, name, description, category, source_url, created_at, updated_at
   - Indexed by: country_code

3. **government_portals**
   - Stores official government resources
   - Fields: id, country_code, portal_name, url, description, category, created_at, updated_at
   - Indexed by: country_code

4. **conversations**
   - Stores conversation history for analysis
   - Fields: id, user_id, country_code, user_message, bot_response, created_at
   - Indexed by: user_id, country_code

## Development Workflow

### 1. Initial Setup
```bash
cd backend
cp .env.example .env
# Edit .env with your credentials
pip install -r requirements.txt
python seed_data.py  # or run SQL migration
python app.py
```

### 2. Testing
```bash
# In another terminal
curl http://localhost:5000/api/health
curl http://localhost:5000/api/countries
```

### 3. Development
- Modify source files as needed
- Flask auto-reloads with FLASK_DEBUG=True
- Check `USAGE_EXAMPLES.md` for testing patterns

### 4. Adding Data
- Edit `seed_data.py` with your research
- Run `python seed_data.py` to update database
- Or insert directly via Supabase dashboard

### 5. Deployment
- Set environment variables in production
- Use Gunicorn or similar WSGI server
- Deploy to cloud platform (Heroku, AWS, Google Cloud, etc.)

## Architecture Overview

```
User Request
    ↓
Flask App (app.py)
    ↓
Session Manager (conversation_manager.py)
    ├─ Creates/manages sessions
    └─ Handles conversation flow
        ↓
    Checks if out-of-context (gemini_service.py)
        ↓
    Retrieves relevant data (database.py)
        ├─ Laws
        ├─ Guidelines
        └─ Portals
        ↓
    Generates AI response (gemini_service.py)
        ├─ Uses system prompt
        └─ Calls Gemini Pro API
        ↓
    Saves conversation (database.py)
        ↓
Returns response to user
```

## Dependencies

### Core Framework
- `Flask==3.0.0` - Web framework
- `Flask-CORS==4.0.0` - Cross-Origin Resource Sharing

### AI Integration
- `google-generativeai==0.3.0` - Google Gemini API client

### Database
- `supabase==2.3.4` - Supabase Python client

### Utilities
- `python-dotenv==1.0.0` - Environment variable management
- `requests==2.31.0` - HTTP client

## Configuration Variables

### Environment (.env)
```
FLASK_ENV=development          # development or production
FLASK_DEBUG=True               # Enable Flask debug mode
PORT=5000                      # Server port

GEMINI_API_KEY=xxx             # Google Gemini API key
SUPABASE_URL=xxx               # Supabase project URL
SUPABASE_KEY=xxx               # Supabase anon key
SUPABASE_SERVICE_KEY=xxx       # Supabase service role key
```

## API Response Examples

### Success Response
```json
{
  "response": "Detailed answer about cybersecurity topic",
  "country": "NYC",
  "is_redirect": false,
  "success": true
}
```

### Error Response
```json
{
  "error": "Error message description",
  "success": false
}
```

### Redirect Response (Out-of-Context)
```json
{
  "response": "I specialize in cybersecurity topics...",
  "country": "NYC",
  "is_redirect": true,
  "success": true
}
```

## File Modification Guide

### To Add New Countries
1. Update `constants.py` - Add country to COUNTRIES dict
2. Update `seed_data.py` - Add laws, guidelines, portals
3. Update `app.py` - Add country to valid_countries list in `/api/session/create`
4. Run `seed_data.py` to populate database

### To Add New Endpoints
1. Add route in `app.py` using `@app.route()` decorator
2. Implement handler function
3. Return JSON response
4. Update `README.md` with documentation

### To Modify AI Behavior
1. Edit system prompt in `constants.py` SYSTEM_PROMPTS
2. Adjust `gemini_service.py` `create_system_prompt()` method
3. Modify out-of-context keywords in `constants.py`

### To Change Database Schema
1. Create new migration in `supabase/migrations/`
2. Run migration in Supabase SQL editor
3. Update `database.py` with new query methods
4. Update `seed_data.py` if adding new tables

## Performance Considerations

- Conversations indexed by user_id and country_code
- Laws/guidelines indexed by country_code
- Supabase automatically caches frequently accessed data
- Session state stored in-memory for fast access
- Gemini API calls are the slowest operation (1-3 seconds typical)

## Security Features

- Row Level Security (RLS) enabled on all tables
- Public read access to laws/guidelines/portals
- Input validation on all endpoints
- CORS enabled for frontend integration
- Environment variables for sensitive data
- No sensitive data logged

## Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| API key not found | Check `.env` has GEMINI_API_KEY |
| Supabase connection failed | Verify URL and keys in `.env` |
| Port already in use | Change PORT in `.env` |
| No database tables | Run `python seed_data.py` |
| CORS errors | Check Flask-CORS configuration in `app.py` |
| Slow responses | Check Gemini API rate limits |

## Next Steps

1. **Start Server:** `python app.py`
2. **Test API:** `curl http://localhost:5000/api/health`
3. **Read Documentation:** See `README.md` for detailed info
4. **Add Data:** Edit `seed_data.py` with your research
5. **Integrate Frontend:** Connect React app to this backend
6. **Deploy:** Use Docker or cloud platform

## Support Resources

- **Gemini API:** https://ai.google.dev/
- **Supabase:** https://supabase.com/docs
- **Flask:** https://flask.palletsprojects.com/
- **Python:** https://docs.python.org/3/

## File Statistics

- **Total Python Files:** 6 (app.py, config.py, database.py, gemini_service.py, conversation_manager.py, constants.py, seed_data.py)
- **Documentation Files:** 4 (README.md, QUICKSTART.md, USAGE_EXAMPLES.md, INDEX.md)
- **Configuration Files:** 2 (.env.example, requirements.txt)
- **Utility Scripts:** 1 (run.sh)
- **Total Files:** 13

---

**Last Updated:** November 2024
**Python Version:** 3.8+
**Flask Version:** 3.0.0
**Status:** Production Ready
