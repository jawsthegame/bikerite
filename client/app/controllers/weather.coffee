Quips     = require 'quips'
Deferred  = require('jqueryify').Deferred
getJSON   = require('jqueryify').getJSON

WeatherDataView  = require 'views/weather/data'


class WeatherController extends Quips.Controller
  layout: require 'templates/weather/layout'

  views:
    '#data': 'dataView'

  routes:
    'weather/': 'show'

  constructor: ->
    @dataView = new WeatherDataView
    super

  show: ->
    @_getData().done (data) => @dataView.render(data)
    @activate()

  _getData: ->
    deferred = new Deferred
    @dataView.block message: 'Loading Weather Data...'
    navigator.geolocation.getCurrentPosition (pos) =>
      url = "#{Quips.host}/weather/#{pos.coords.latitude},#{pos.coords.longitude}"
      getJSON(url).done (result) =>
        @dataView.unblock()
        deferred.resolve(result)

    deferred.promise()


module.exports = WeatherController
