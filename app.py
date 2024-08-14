import requests

def get_pun():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        return joke.get('joke', "No pun found.")
    else:
        return "Failed to retrieve a pun."

if __name__ == "__main__":
    pun = get_pun()
    print("Here's a pun for you:")
    print(pun)
