import requests

prefix_url = 'https://api.duckduckgo.com/?q='
search_term = 'presidents+of+the+united+states'
postfix_url = '&format=json'
url = prefix_url + search_term + postfix_url


r = requests.get(url)

response = r.json()

print(response['RelatedTopics'])