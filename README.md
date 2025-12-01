# Serverless Sentiment Analysis API

A cloud-native microservice that performs Natural Language Processing (NLP) to determine the sentiment (Positive/Negative/Neutral) of user text. Deployed on **AWS Lambda** using Serverless architecture.

## Architecture
* **Compute:** AWS Lambda (Serverless)
* **Language:** Python 3.x
* **AI Engine:** VaderSentiment (NLTK-based logic)
* **Infrastructure:** AWS Function URL (HTTPS Endpoint)

## 🌐 Public Endpoint
The API is currently live on AWS Lambda. You can test it using `curl`, Postman, or PowerShell.

**Base URL:**
`https://s2i3rtxm4uxdawwlpu4e6q42pq0hmfum.lambda-url.us-east-1.on.aws/`

### Quick Test (Copy & Paste into Terminal)
```powershell
curl -X POST "https://s2i3rtxm4uxdawwlpu4e6q42pq0hmfum.lambda-url.us-east-1.on.aws/" \
     -H "Content-Type: application/json" \
     -d '{"text": "I am impressed by this cloud architecture."}'
     
## Usage
Send a POST request to the API endpoint with a JSON body:
{
  "text": "The service is running perfectly."
}

## Example Response
{
  "mood": "POSITIVE",
  "confidence": 0.6369,
  "breakdown": {
    "neg": 0.0,
    "neu": 0.412,
    "pos": 0.588,
    "compound": 0.6369
  }
}

## Local Development
1. Clone the repo.
2. Create a virtual env: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run locally: `python app.py`