import json
from logic import analyze_mood

def lambda_handler(event, context):
    # 1. AWS sends data in an 'event' object
    # We need to parse the body string into a JSON dictionary
    try:
        body = json.loads(event['body'])
        user_text = body.get('text', '')
    except:
        user_text = "No text provided"

    # 2. Call your AI Brain
    result = analyze_mood(user_text)

    # 3. Return the response in the format AWS API Gateway expects
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }