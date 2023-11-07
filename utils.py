import requests



def load_random_word(url):
    response = requests.get(url)
    print("HTTP Status Code:", response.status_code)  # Add this line to print the status code
    if response.status_code == 200:
        data = response.json()
        word = data["word"]
        subwords = data["subwords"]
        return BasicWord(word, subwords)
    else:
        print("Failed to load random word.")
        return None
