import time
from riotwatcher import LolWatcher, ApiError


lol_watcher = LolWatcher('RGAPI-xxx') ####your api key here

region = 'na1'

me=lol_watcher.summoner.by_name(region, 'dubayoo')

print(me)

try:
    current = lol_watcher.spectator.by_summoner(region, "tix9yy2IJjRJ3ggnFnXIG1V8EeUjWQm6fEau7ud8cmkTdSpO8xLvdOJ2yQ")
except ApiError as err:
    if err.response.status_code == 404:
        print("not in game")
    elif err.response.status_code == 400:
        print("wrong id")
else:
    print(current)

