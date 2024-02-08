import requests

url = "http://127.0.0.1:5000/prediction"

data = {'sepal_length': 5.1,
    'sepal_width': 3.5,
    'petal_length': 1.4,
    'petal_width': 0.2}

# Send the GET request to the API
response = requests.get(url, params=data)

# Check the API's response
if response.status_code == 200:
    predictions = response.json()
    print("Prédictions :", predictions)
else:
    print("Erreur lors de la requête :", response.status_code)