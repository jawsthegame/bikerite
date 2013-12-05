Quips     = require 'quips'
$         = require 'jqueryify'
Backbone  = require 'backbone'

WeatherController  = require 'controllers/weather'


class App

  constructor: (config) ->
    Quips.host = config?.host
    @showUI()

  showUI: ->
    $layout = $('body').empty().append(require 'templates/layout')
    $content = $layout.find('#main-content')

    new WeatherController(el: $content)

    Backbone.history.start()

    unless window.location.hash
      Backbone.history.navigate '#/weather'


module.exports = App
