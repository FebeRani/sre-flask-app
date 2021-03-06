from config import hello
from flask import jsonify,request
from Model import employee,person

@hello.route("/Employee")
def getPeople():
    listp=employee.getEmployee()
    result = [x.serialize() for x in listp]
    return jsonify(result)

    @hello.route("/employee",methods=['POST'])
    def addEmployee():
        input=request.get_json()
        employeeno=input['employeeno']
        name=input['name']
        city=input['city']
        desig=input['desig']
        newitem=person(employeeno,name,city,desig)
        employee.addEmployee(newitem)
        return "item added successfully"