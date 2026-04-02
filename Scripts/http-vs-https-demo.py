# Simple demo to show HTTP vs HTTPS request
import requests

http_url = "http://example.com"
https_url = "https://example.com"

# HTTP request
http_response = requests.get(http_url)
print(f"HTTP status: {http_response.status_code}")

# HTTPS request
https_response = requests.get(https_url)
print(f"HTTPS status: {https_response.status_code}")
