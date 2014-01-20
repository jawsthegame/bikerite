from flask import Blueprint
from json import dumps

from bikerite.lib.wunderground import get_weather


weather = Blueprint('weather', __name__)

WARN  = 'If you have to bike, be careful out there!'
AVOID = 'I would seriously recommend you do not ride today.'

@weather.route("/<lat>,<lon>")
def get_weather_by_position(lat, lon):
  data = get_weather(lon, lat)
  data['wear'] = _get_wear(data)
  data['warning'] = _get_warning(data)
  if data['precip_today_in'] < 0:
    data['precip_today_in'] = 0
  return dumps(data)

def _get_warning(data):
  weather = data['weather'].lower()
  temp    = data['temp_f']
  wind    = data['wind_mph']

  maybe = ['light drizzle', 'light rain', 'light snow']
  avoid = ['heavy', 'ice', 'thunderstorm', 'freezing', 'blowing',
    'showers', 'hail', 'rain', 'snow']

  if wind > 20 or temp < 15 or temp > 95:
    return ['avoid', AVOID]
  elif [m for m in maybe if m in weather]:
    return ['warn', WARN]
  elif [av for av in avoid if av in weather]:
    return ['avoid', AVOID]

def _get_wear(data):
  temp = data['temp_f']
  wind = data['wind_mph']

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
  BALACL  = 'a balaclava'

  if temp > 70:
    wear = [TSHIRT, SHORTS]
  elif temp > 65:
    wear = [TSHIRT, JEANS]
  elif temp > 60:
    wear = [HOODIE, JEANS]
  elif temp > 55:
    wear = [HOODIE, LIGHT_J, JEANS]
  elif temp > 48:
    wear = [HOODIE, MED_J, JEANS, GLOVES]
  elif temp > 38 and wind < 5:
    wear = [HOODIE, MED_J, JEANS, SCARF, GLOVES]
  elif temp > 38:
    wear = [HOODIE, MED_J, JEANS, SCARF, GLOVES, WOOL_H]
  elif temp > 30 and wind < 5:
    wear = [HEAVY_C, JEANS, SCARF, GLOVES, WOOL_H]
  else:
    wear = [HEAVY_C, GLOVES, SCARF, JEANS, BALACL]

  return _format_list(wear)

def _format_list(items):
  if len(items) > 2:
    return ' and '.join([', '.join(items[:-1]), items[-1]])
  else:
    return ' and '.join(items)
