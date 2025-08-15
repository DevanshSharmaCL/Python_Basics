import requests

# Example: Fetch a random joke
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

# Convert response to Python dictionary
data = response.json()

print(f"Here's a joke: {data['setup']} - {data['punchline']}")
