from flask import Flask, request, jsonify
from cache import cache
from pathlib import Path


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
            #print(f'items is truthy {items}' if items else f'Items is falsey {items}')
            return str(items), 200 if items else 'no items'

        elif request.method == 'DELETE':
            cache.clear()
            print('deleted cache:')
            return 'items have been discarded'

    except TypeError:
        print('type error')
        return "no items"


if __name__ == '__main__':
    app.run(debug = True)

