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
    return jsonify(garage_DB)

# Add cars to garage and level
@app.route("/add", methods=['POST'])
def add():

    try:
        req = request.get_json()
        garage_name = req['garage']
        level = req['lvl']
        # print garage_DB[garage_name]
        garage_DB[garage_name]["lvlarr"][level - 1][2] -= 1

        garage_DB[garage_name]["available"] -= 1
        garage_DB[garage_name]["occupied"] += 1

        return jsonify(garage_DB)

    except:
        return "Fail"

# Remove cars from garage and level
@app.route("/remove", methods=['POST'])
def remove():
    try:
        req = request.get_json()
        garage_name = req['garage']
        level = req['lvl']

        garage_DB[garage_name]["lvlarr"][level - 1][2] += 1

        garage_DB[garage_name]["available"] += 1
        garage_DB[garage_name]["occupied"] -= 1

        return jsonify(garage_DB)
    except:
        return "Fail"


# Add new garage
@app.route("/addgarage", methods=['POST'])
def addGarage():
    try:
        # get and parse json
        req = request.get_json()
        garage_name = req['name']
        levelarr = req['lvlarr']
        
        # add data
        garage_DB[garage_name] = {}
        garage_DB[garage_name]["name"] = garage_name
        garage_DB[garage_name]["lvlarr"] = [[levelNumber, total, total] for levelNumber, total in levelarr]
        total = 0
        for _,levelSpace in levelarr:
            total+=levelSpace
        garage_DB[garage_name]["total"] = total
        garage_DB[garage_name]["occupied"] = 0
        garage_DB[garage_name]["available"] = total
        return jsonify(garage_DB)
    except:
        return "Fail"

# Remove garage
@app.route("/removegarage", methods=['POST'])
def removeGarage():
    try:
        # get and parse json
        req = request.get_json()
        garage_name = req['name']
        
        if not garage_DB.has_key(garage_name):
            return "Garage doesn't exist. Bad request."
        
        garage_DB.pop(garage_name, None)
        return jsonify(garage_DB)
    except:
        return "Fail"

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000)
