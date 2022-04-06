#! /usr/bin/env python3

from flask import Flask, request, jsonify
from cache import cache
from pathlib import Path

class Item():
    def __init__(self, identifier, name):
        self.item = {'id': identifier, 'name': name}


app = Flask(__name__)

cache.init_app(app=app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': Path('/tmp')})

@app.route('/items',methods = ['POST', 'GET', 'DELETE'])
def web_people():
    try:
        if request.method == 'POST':
            '''POST requires a list of dicts, each dict contains values for "id" and "name"'''
            people = list(request.get_json())
            print(people)
            #print([f'{key}: {val}' for item[0] in people.list()]
            #print([f'{ident}: {name}') for item['id'], item] in people]
            cache.set('db',people)
            print(people[0].item['id'])
            print(people[0].item['name'])
            return 'post complete'

        elif request.method == 'GET':
            '''GET returns a list of dicts, each dict contains values for "id" and "name"'''
            print('processing GET')
            people = cache.get('db')
            people = [str(item) for item in people]
            print(people)
            return str(people)

        elif request.method == 'DELETE':
            cache.clear()
            print('deleted cache:')
            return 'people have been discarded'

    except TypeError:
        print('type error')
        return "no people"


if __name__ == '__main__':
    app.run(debug = True)

