# Serverless Sentiment Analysis API

A cloud-native microservice that performs Natural Language Processing (NLP) to determine the sentiment (Positive/Negative/Neutral) of user text. Deployed on **AWS Lambda** using Serverless architecture.

## Architecture
* **Compute:** AWS Lambda (Serverless)
* **Language:** Python 3.x
* **AI Engine:** VaderSentiment (NLTK-based logic)
* **Infrastructure:** AWS Function URL (HTTPS Endpoint)

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