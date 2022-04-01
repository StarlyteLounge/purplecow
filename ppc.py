from flask import Flask, request, jsonify


app = Flask(__name__)

items = {'a':1,'b':2}

@app.route('/items',methods = ['POST', 'GET', 'DELETE'])
def web_items():
    try:
        if request.method == 'POST':
            item_list = list(request.get_json())
            print(type(item_list))
            print(item_list)
            return 'post complete'

        elif request.method == 'GET':
            print('processing GET')
            print(items)
            return items, 200 if items else 'no items'

        elif request.method == 'DELETE':
            item_list.clear()
            print(item_list)
            print('deleted cache:')
            return 'items have been discarded'

    except TypeError:
        print('type error')
        return "no items"


if __name__ == '__main__':
    app.run(debug = True)

