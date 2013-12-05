import requests


KEY = 'beaf09e591898ab1'


def get_weather(lon, lat):
  url = ('http://api.wunderground.com/api/%s' + \
          '/conditions/q/%s,%s.json') % (KEY, lat, lon)
  resp = requests.get(url)
  return resp.json()['current_observation']
