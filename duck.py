import requests

pres_list = ("Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tyler",
"Polk","Taylor", "Fillmore","Pierce", "Buchanan","Lincoln", "Johnson","Grant", "Hayes","Garfield", "Arthur", "Cleveland",
"Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt",
"Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama",
"Trump", "Biden")

prefix_url = 'https://api.duckduckgo.com/?q='
search_term = 'presidents+of+the+united+states'
postfix_url = '&format=json'
url = prefix_url + search_term + postfix_url

text_string = ''
text_list = list()
r = requests.get(url)

response = r.json()
related_topics = response['RelatedTopics']

for item in related_topics:
    text_list.append(item['Text'])
    text_string += ' ' + item['Text']

print(text_list)
for pres in pres_list:
    print(pres)
    if pres not in text_string:
        print(pres + 'not in')


# print(response['RelatedTopics'][0]['Text'])