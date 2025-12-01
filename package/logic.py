from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

def analyze_mood(text_input):
    # Initialize the AI analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Ask the AI to score the text
    scores = analyzer.polarity_scores(text_input)
    
    # Logic to decide the human-readable label
    compound_score = scores['compound']
    
    if compound_score >= 0.05:
        mood = "POSITIVE"
    elif compound_score <= -0.05:
        mood = "NEGATIVE"
    else:
        mood = "NEUTRAL"

    # Return a dictionary (perfect for API responses later)
    return {
        "text": text_input,
        "mood": mood,
        "confidence": compound_score,
        "breakdown": scores
    }

# Quick test if running this file directly
if __name__ == "__main__":
    test_text = "I am seriously impressed with how fast this server is!"
    print(json.dumps(analyze_mood(test_text), indent=2))