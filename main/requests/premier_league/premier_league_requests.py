import json
import time
import requests


# ***** Requests API and creates JSON-Files with response. *****

years = list(range(2010, 2020 + 1))

for year in years:
    url = f"https://v3.football.api-sports.io/fixtures?league=39&season={year}"

    payload = {}
    # XxXxXxXxXxXxXxXxXxXxXxXx
    headers = {
        'x-rapidapi-key': 'fd1348bd73ce135ca127ddbe078ca0b8',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    myjson = json.loads(response.text)

    with open(f'../../resources/premier_league/premier_league_{year}.json', 'w', encoding='utf-8') as outfile:
        json.dump(myjson, outfile, ensure_ascii=False, indent=4)

    # only 10 requests per minute allowed
    time.sleep(6)
