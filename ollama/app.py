"""
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Hola",
  "stream":false
}'
"""

import requests
import json

url = "http://localhost:11434/api/generate"

data  = {
  "model": "gemma3:1b",
  "prompt":"Hola",
  "stream":False
}

response = requests.post(url, json=data)

response = json.loads(response.text)

print(response["response"])
