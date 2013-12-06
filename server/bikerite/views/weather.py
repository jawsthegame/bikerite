from flask import Blueprint
from json import dumps

from bikerite.lib.wunderground import get_weather


weather = Blueprint('weather', __name__)

@weather.route("/<lat>,<lon>")
def get_weather_by_position(lat, lon):
  data = get_weather(lon, lat)
  data['wear'] = _get_wear(data)
  if data['precip_today_in'] < 0:
    data['precip_today_in'] = 0
  return dumps(data)

def _get_wear(data):
  temp = data['temp_f']

  TSHIRT  = 'a t-shirt'
  SHORTS  = 'shorts'
  JEANS   = 'jeans'
  LONG_SL = 'long sleeves'
  HOODIE  = 'a hoodie'
  LIGHT_J = 'a light jacket'
  MED_J   = 'a medium jacket'
  GLOVES  = 'gloves'
  SCARF   = 'a scarf'
  HEAVY_C = 'a heavy coat'
  WOOL_H  = 'a wool hat'

  if temp > 70:
    wear = [TSHIRT, SHORTS]
  elif temp > 65:
    wear = [TSHIRT, JEANS]
  elif temp > 60:
    wear = [LONG_SL, JEANS]
  elif temp > 55:
    wear = [HOODIE, JEANS]
  elif temp > 48:
    wear = [HOODIE, LIGHT_J, JEANS]
  elif temp > 34:
    wear = [HOODIE, MED_J, JEANS, GLOVES]
  elif temp > 30:
    wear = [HEAVY_C, GLOVES, SCARF, JEANS]
  else:
    wear = [HEAVY_C, GLOVES, SCARF, JEANS, WOOL_H]

  return _format_list(wear)

def _format_list(items):
  if len(items) > 2:
    return ' and '.join([', '.join(items[:-1]), items[-1]])
  else:
    return ' and '.join(items)
