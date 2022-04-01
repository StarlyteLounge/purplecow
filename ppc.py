from flask import Flask, request, jsonify
from cache import cache
from pathlib import Path

class Item():
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name

app = Flask(__name__)

cache.init_app(app=app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': Path('/tmp')})

@app.route('/items',methods = ['POST', 'GET', 'DELETE'])
def web_items():
    try:
        if request.method == 'POST':
            item_list = list(request.get_json())
            print(type(item_list))
            cache.set('db',item_list)
            print(item_list)
            return 'post complete'

        elif request.method == 'GET':
            print('processing GET')
            items = cache.get('db')
            print(items)
            return str(items)

        elif request.method == 'DELETE':
            cache.clear()
            print('deleted cache:')
            return 'items have been discarded'

    except TypeError:
        print('type error')
        return "no items"


if __name__ == '__main__':
    app.run(debug = True)

