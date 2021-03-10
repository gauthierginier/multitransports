from flask import render_template, jsonify

from multitransports.back.requestsapi import *


def entry_point():
    return render_template('./index.html')

def hello_world():
    return 'Hello Boug'

def nexttram(station, ville):
    """This function connect to db for
    execute the function requestnexttram and
    return json.

    station : is the station to select for see the next
    tramway in this station

    ville : Is the city for search station 
    in this city

    """
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    res = requestnexttram(c, station, ville)
    return jsonify(res)

def citystations(ville):
    """This function connect to db for
    execute the function request_city_station
    and return json.

    ville : Is the city for search station 
    in this city

    """
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    res = request_city_station(c, ville)
    return jsonify(res)

def line_station(ville, ligne):
    """This function connect to db for
    execute the function request_line_station
    and return json.

    ville : Is the city for search station 
    in this city

    ligne : is the line to select for see all
    stations in this line

    """
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    res = request_line_station(c, ville, ligne)
    return jsonify(res)

def next_to_direction(ville, station, ligne, direction):
    """
    This function connect to db for
    execute the function request_next_to_direction
    and return json.

    ville : Is the city for search station 
    in this city

    ligne : is the line to select for see all
    stations in this line

    station : is the station to select for see the next tramway in 
    this station

    direction : Is the direction select for see the next tramway in
    this direction

    """
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    res = request_next_to_direction(c, ville, station, ligne, direction)
    return jsonify(res)

def station_like(station, ville):
    """This function connect to db for
    execute the function request_station_like and
    return json.

    station : is the station to select for see the next
    tramway in this station

    ville : Is the city for search station 
    in this city

    """
    conn = sqlite3.connect('transport.db')
    c = conn.cursor()
    res = request_station_like(c,station,ville)
    return jsonify(res)