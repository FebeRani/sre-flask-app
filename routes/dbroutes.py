from config import app,Db
from flask import jsonify,request
from Model import employee,Dbperson

@app.route("/Employee")
def getDbEmployee():
    listp=Dbperson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)