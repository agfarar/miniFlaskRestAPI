from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

names = {"tim":{"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}

class HelloWorld(Resource):

    def get(self, name):
        #return {"data": name}
        return names[name]
    
    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")# endpoint




if __name__ == "__main__":
    app.run(debug = True) #Not in production
