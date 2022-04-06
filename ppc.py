#! /usr/bin/env python3

import json
from flask import Flask, request, jsonify
from cache import cache
from pathlib import Path

class Item():
    def __init__(self, identifier, name):
        self.item = {'id': identifier, 'name': name}


app = Flask(__name__)
app.config.from_file('settings.cfg', load=json.load)

cache.init_app(app=app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': Path('/tmp')})

@app.route('/items',methods = ['POST', 'GET', 'DELETE'])
def web_people():
    try:
        if request.method == 'POST':
            '''POST requires a list of dicts, each dict contains values for "id" and "name"'''
            people = list(request.get_json())
            cache.set('db',people)
            return 'post complete'

        elif request.method == 'GET':
            '''GET returns a list of dicts, each dict contains values for "id" and "name"'''
            people = cache.get('db')
            people = [str(item) for item in people]
            return str(people)

        elif request.method == 'DELETE':
            cache.clear()
            return 'people have been discarded'

    except TypeError:
        return "no people"


if __name__ == '__main__':
    app.run(debug = True)

