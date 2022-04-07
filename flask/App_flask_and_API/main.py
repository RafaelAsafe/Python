from logging import debug
from os import name
from flask import Flask, request, jsonify
#from .src import itens
app = Flask(__name__)

stores = [
    {
        "name": "Asa Store",
        "itens": [
            {
                "name": "My itens",
                "price": 13.59
            }
        ]
    }
]

# POST -- used to receive data
# GET --user to send data back only

# POST /store data:(name:)


@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass

# GET /store


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item{name:,price:}


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
    pass

# GET /store/<string:name>/item


@app.route('/store/<string:name>/item', methods=['GET'])
def get_item(name):
    pass


app.run(
    port=5000,
    debug=True
)
