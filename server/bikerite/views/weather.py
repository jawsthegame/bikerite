from flask import Blueprint
from json import dumps

from bikerite.lib.wunderground import get_weather


weather = Blueprint('weather', __name__)

@weather.route("/<lat>,<lon>")
def get_weather_by_position(lat, lon):
  return dumps(get_weather(lon, lat))
