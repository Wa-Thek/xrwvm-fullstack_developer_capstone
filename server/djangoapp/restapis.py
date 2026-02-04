# Uncomment the imports below before you add the function code
import requests
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Remove trailing slash from sentiment_analyzer_url if present
if sentiment_analyzer_url and sentiment_analyzer_url.endswith('/'):
    sentiment_analyzer_url = sentiment_analyzer_url[:-1]

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

def analyze_review_sentiments(text):
    # FIX: Use path parameter instead of query parameter
    # URL encode the text for use in path
    encoded_text = urllib.parse.quote(text)
    request_url = f"{sentiment_analyzer_url}/analyze/{encoded_text}"
    
    print(f"DEBUG: Calling sentiment analyzer at: {request_url}")
    
    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Sentiment analysis failed: {e}")
        return None
    except Exception as err:
        print(f"Unexpected error: {err}")
        return None

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None