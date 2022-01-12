import json
import time
import requests

# ***** Requests API and creates JSON-Files with response. *****

years = list(range(2010, 2020 + 1))

for year in years:
    url = f"https://v3.football.api-sports.io/fixtures?league=78&season={year}"

    payload = {}
    headers = {
        'x-rapidapi-key': 'XxXxXxXxXxXxXxXxXxXxXxXx',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    myjson = json.loads(response.text)

    with open(f'../../../resources/bundesliga/bundesliga_{year}.json', 'w', encoding='utf-8') as outfile:
        json.dump(myjson, outfile, ensure_ascii=False, indent=4)

    # only 10 requests per minute allowed
    time.sleep(6)
