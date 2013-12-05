Quips = require 'quips'
$     = require 'jqueryify'


class WeatherDataView extends Quips.View
  template: ->
    tmpl = require 'templates/weather/data'
    tmpl data: @data

  render: (@data) ->
    super

module.exports = WeatherDataView
