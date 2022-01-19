import json
import time
import requests

# ***** Requests API and creates JSON-Files with response. *****

years = list(range(2010, 2020 + 1))

for year in years:
    # id  muss geändert werden
    url = f"https://v3.football.api-sports.io/fixtures?league=61&season={year}"

    payload = {}
    # zugangs login für football api
    headers = {
        # api key hier hin nach push und commit wieder mit x'en
        # fd1348bd73ce135ca127ddbe078ca0b8 XxXxXxXxXxXxXxXxXxXxXxXx
        'x-rapidapi-key': 'XxXxXxXxXxXxXxXxXxXxXxXx',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    # https anfragen protokoll handshake etc.
    response = requests.request("GET", url, headers=headers, data=payload)

    # in json umkonvertieren
    myjson = json.loads(response.text)

    # hier den pfad ändern
    with open(f'../../resources/ligue_1/ligue_1_{year}.json', 'w', encoding='utf-8') as outfile:
        json.dump(myjson, outfile, ensure_ascii=False, indent=4)

    # only 10 requests per minute allowed
    time.sleep(6)