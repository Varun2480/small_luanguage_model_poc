import requests


# url = "https://small-luanguage-model-poc.onrender.com/restaurant/"
# url = "http://127.0.0.1:8000/restaurant/"
url = "http://127.0.0.1:8000/privacy/"

payload = {
    "dish_name": "Pizza",
    "dish_type": "veg",
    "budget": 350
}

# response = requests.post(url=url, json=payload)
response = requests.get(url=url)

if response.status_code == 200:
    # Successful response
    data = response.json()  # Get the JSON data from the response
    print(data)  # Print the data
else:
    # Error handling
    print(f"Error: {response.status_code}")
    print(response.text) 