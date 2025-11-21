# Chatbot Usage Examples

This guide demonstrates how to use the Cybersecurity Chatbot API with practical examples.

## Example 1: Complete Conversation Flow

### Step 1: Create a Session

```bash
curl -X POST http://localhost:5000/api/session/create \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user_123",
    "country_code": "NYC"
  }'
```

Response:
```json
{
  "session_id": "abc123def456",
  "user_id": "user_123",
  "country_code": "NYC",
  "message": "Welcome! I am your cybersecurity compliance advisor. How can I assist you today?"
}
```

### Step 2: Ask a Question

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "abc123def456",
    "message": "What are the key requirements of the New York SHIELD Act?"
  }'
```

Response:
```json
{
  "response": "The New York SHIELD Act (Stop Hacks and Improve Electronic Data Security) is a comprehensive data protection law that requires businesses to implement reasonable safeguards for personal information. Key requirements include...",
  "country": "NYC",
  "is_redirect": false,
  "success": true
}
```

### Step 3: Continue the Conversation

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "abc123def456",
    "message": "What are the penalties for non-compliance?"
  }'
```

The chatbot maintains context from the previous message.

### Step 4: Switch Country

```bash
curl -X POST http://localhost:5000/api/session/abc123def456/switch-country \
  -H "Content-Type: application/json" \
  -d '{
    "country_code": "GERMANY"
  }'
```

Response:
```json
{
  "success": true,
  "message": "Switched to GERMANY cybersecurity compliance advisor",
  "country_code": "GERMANY"
}
```

### Step 5: Ask About Germany

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "abc123def456",
    "message": "What is GDPR and how does it affect German businesses?"
  }'
```

### Step 6: End Session

```bash
curl -X POST http://localhost:5000/api/session/abc123def456/end \
  -H "Content-Type: application/json"
```

Response:
```json
{
  "success": true,
  "message": "Session ended"
}
```

## Example 2: Out-of-Context Handling

### User Asks an Off-Topic Question

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "abc123def456",
    "message": "What's the weather like today?"
  }'
```

Response:
```json
{
  "response": "I appreciate your question, but I specialize in cybersecurity compliance topics for NYC. Let's refocus on your cybersecurity concerns. Could you tell me about specific compliance or security topics you'd like to discuss?",
  "country": "NYC",
  "is_redirect": true,
  "success": true
}
```

## Example 3: Multiple Countries Session

```bash
# Create session for South Korea
curl -X POST http://localhost:5000/api/session/create \
  -H "Content-Type: application/json" \
  -d '{
    "country_code": "SOUTH_KOREA"
  }'
```

## Example 4: Python Client Implementation

```python
import requests

class ChatbotClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.session_id = None

    def create_session(self, country_code="NYC"):
        response = requests.post(
            f"{self.base_url}/api/session/create",
            json={"country_code": country_code}
        )
        self.session_id = response.json()["session_id"]
        return response.json()

    def send_message(self, message):
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "session_id": self.session_id,
                "message": message
            }
        )
        return response.json()

    def switch_country(self, country_code):
        response = requests.post(
            f"{self.base_url}/api/session/{self.session_id}/switch-country",
            json={"country_code": country_code}
        )
        return response.json()

    def end_session(self):
        response = requests.post(
            f"{self.base_url}/api/session/{self.session_id}/end"
        )
        return response.json()

# Usage
client = ChatbotClient()

# Create session
session = client.create_session("NYC")
print(f"Session created: {session['message']}")

# Ask questions
response = client.send_message("What is HIPAA?")
print(f"Bot: {response['response']}")

response = client.send_message("How does HIPAA affect healthcare providers?")
print(f"Bot: {response['response']}")

# Switch country
client.switch_country("GERMANY")
print("Switched to Germany")

response = client.send_message("What is GDPR?")
print(f"Bot: {response['response']}")

# End session
client.end_session()
print("Session ended")
```

## Example 5: JavaScript/Fetch Implementation

```javascript
class ChatbotClient {
    constructor(baseUrl = "http://localhost:5000") {
        this.baseUrl = baseUrl;
        this.sessionId = null;
    }

    async createSession(countryCode = "NYC") {
        const response = await fetch(`${this.baseUrl}/api/session/create`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ country_code: countryCode })
        });
        const data = await response.json();
        this.sessionId = data.session_id;
        return data;
    }

    async sendMessage(message) {
        const response = await fetch(`${this.baseUrl}/api/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                session_id: this.sessionId,
                message: message
            })
        });
        return await response.json();
    }

    async switchCountry(countryCode) {
        const response = await fetch(
            `${this.baseUrl}/api/session/${this.sessionId}/switch-country`,
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ country_code: countryCode })
            }
        );
        return await response.json();
    }

    async endSession() {
        const response = await fetch(
            `${this.baseUrl}/api/session/${this.sessionId}/end`,
            { method: "POST" }
        );
        return await response.json();
    }
}

// Usage
const client = new ChatbotClient();

(async () => {
    // Create session
    const session = await client.createSession("NYC");
    console.log("Session created:", session.message);

    // Ask questions
    let response = await client.sendMessage("What is the SHIELD Act?");
    console.log("Bot:", response.response);

    response = await client.sendMessage("Who needs to comply?");
    console.log("Bot:", response.response);

    // Switch country
    await client.switchCountry("SOUTH_KOREA");
    console.log("Switched to South Korea");

    response = await client.sendMessage("What is PIPA?");
    console.log("Bot:", response.response);

    // End session
    await client.endSession();
    console.log("Session ended");
})();
```

## Example 6: Conversation Topics

### NYC Examples
- "What is the SHIELD Act?"
- "What are HIPAA requirements for hospitals?"
- "How do data breach notifications work in New York?"
- "What are the penalties for SHIELD Act violations?"

### Germany Examples
- "Explain GDPR requirements"
- "What is the BSI IT Security Act?"
- "How does Germany protect critical infrastructure?"
- "What are GDPR fines for violations?"

### South Korea Examples
- "What is PIPA?"
- "Explain the ICN Act"
- "What does KISA do?"
- "How are personal data breaches handled in South Korea?"

## Error Handling Examples

### Invalid Session

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "invalid_session",
    "message": "Hello"
  }'
```

Response:
```json
{
  "error": "Invalid session",
  "success": false
}
```

### Invalid Country Code

```bash
curl -X POST http://localhost:5000/api/session/create \
  -H "Content-Type: application/json" \
  -d '{
    "country_code": "INVALID"
  }'
```

Response:
```json
{
  "error": "Invalid country code",
  "valid_countries": ["NYC", "GERMANY", "SOUTH_KOREA"]
}
```

### Empty Message

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "abc123def456",
    "message": ""
  }'
```

Response:
```json
{
  "error": "Message cannot be empty"
}
```

## Testing with cURL

Quick test commands:

```bash
# Health check
curl http://localhost:5000/api/health

# Get countries
curl http://localhost:5000/api/countries

# Create session and capture session_id
SESSION=$(curl -s -X POST http://localhost:5000/api/session/create \
  -H "Content-Type: application/json" \
  -d '{"country_code":"NYC"}' | jq -r '.session_id')

echo $SESSION

# Send message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"session_id\":\"$SESSION\",\"message\":\"What is cybersecurity?\"}" \
  | jq
```

## Integration with Frontend

The backend is designed to work seamlessly with any frontend framework:

1. **React**: Use `fetch` or `axios` to call the endpoints
2. **Vue**: Similar approach with `fetch` or libraries
3. **Angular**: Use `HttpClient` service
4. **Plain JavaScript**: Use native `fetch` API
5. **Any other framework**: Use standard HTTP requests

See the README.md for frontend integration examples.
