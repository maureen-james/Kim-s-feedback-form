from email.quoprimime import quote
import urllib.request,json
import requests 
# from . import request
from .models import Quote

# # Getting api key
# api_key = None







API = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    Function that consumes http request and returns random quotes
    """
    response = requests.get(API).json()
    random_quote = Quote(response.get("author"), response.get("quote"))
    
    return random_quote