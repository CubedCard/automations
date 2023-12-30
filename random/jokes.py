import requests
import time

api_url = 'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=twopart'
result = requests.get(api_url)
setup, punchline = result.text.split('\n\n')[0], result.text.split('\n\n')[1]

print(setup)
time.sleep(1.5)
print(punchline)
