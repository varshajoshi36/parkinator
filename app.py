from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify
from flask_cors import CORS

# Initialize api
app = Flask(__name__)
CORS(app)
api = Api(app)

# Declare key_value store
garage_DB = {}

# Return parking garage details
@app.route("/read", methods=['GET'])
def read():
    # d = {}
    # d["Creekside"] = {
    #     "name": "Creekside",
    #     "total": 100,
    #     "curr": 20,
    #     "lvlarr": [[1, 30, 10], [2, 30, 10], [3, 40, 0]] 
    # }
    # d["Central"] = {
    #     "name": "Central Garage",
    #     "total": 100,
    #     "curr": 20,
    #     "lvlarr": [[1, 30, 10], [2, 30, 10], [3, 40, 0]] 
    # }
    return jsonify(garage_DB)

# Add cars to garage and level
@app.route("/add")
def add():
    try:
        garage_name = request.args.get('garage')
        level = request.args.get('lvl')
        print garage_name, level
        return "Success"
    except:
        return "Fail"

# Remove cars from garage and level
@app.route("/remove")
def remove():
    try:
        garage_name = request.args.get('garage')
        level = request.args.get('lvl')
        print garage_name, level
        return "Success"
    except:
        return "Fail"

# Add new garage
@app.route("/addgarage")
def addGarage():
    try:
        garage_name = request.args.get('garage')
        level = request.args.get('lvl')
        total = request.args.get('total')
        print garage_name, level, total
        return "Success"
    except:
        return "Fail"

# Remove garage
@app.route("/removegarage")
def removeGarage():
    try:
        garage_name = request.args.get('garage')
        print garage_name
        return "Success"
    except:
        return "Fail"

if __name__ == '__main__':
	 app.run(port=8080)
