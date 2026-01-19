import requests
# see why


def fetch_data(endpoint, filters={}):
    # --- GET ---
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters)

    return response.json() if response.status_code == 200 else None


# Estudar como vem uma response após os filters
# Estudar como é filtrado a response
# O filter é ignorado quando não encontra o correspondente?
characters = fetch_data("character/1", {})
print(characters)
