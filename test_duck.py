import requests

url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


def test_pres():
    pres_list = (
        "Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tyler",
        "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield",
        "Arthur",
        "Cleveland",
        "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover",
        "Roosevelt",
        "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush",
        "Obama",
        "Trump", "Biden")
    prefix_url = 'https://api.duckduckgo.com/?q='
    search_term = 'presidents+of+the+united+states'
    postfix_url = '&format=json'
    url = prefix_url + search_term + postfix_url
    text_string = ''
    r = requests.get(url)
    response = r.json()
    related_topics = response['RelatedTopics']
    for item in related_topics:
        text_string += ' ' + item['Text']
    for pres in pres_list:
        print(pres)
        assert pres in text_string


test_pres()