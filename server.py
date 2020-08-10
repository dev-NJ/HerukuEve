from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from ReadJson import getResponseFromJSON

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)      

@app.route('/botResponse',methods = ['POST', 'GET'])
def BotResponse():
   if request.method == 'POST':
        print('botResponse - POST')
        chatFromUser = request.form.get('chatFromUser')
        chatResponseFromBot = getResponseFromJSON(chatFromUser)
        result = {'data': {'botResponse':chatResponseFromBot}}
        return jsonify(result) 
   else:
        result = {'data': {'botResponse':'Please send request as POST'}}
        return jsonify(result)

    # if request.method == 'POST':
        # data = request.form
   #  else:
      #   pass
    #def post(self): 
       # result = {'data': {'id':1, 'name':'Balram'}}
      #  print('nithin')
     


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
#api.add_resource(BotResponse, '/botResponse')


if __name__ == '__main__':
     app.run(port=5002)
