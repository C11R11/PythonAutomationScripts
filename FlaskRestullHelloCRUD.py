# Resourceful Routing
# The main building block provided by Flask-RESTful are resources.
# Resources are built on top of Flask pluggable views, giving you
# easy access to multiple HTTP methods just by defining methods on
# your resource. A basic CRUD resource for a todo application
# (of course) looks like this:
#
# $ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
# {"todo1": "Remember the milk"}
# $ curl http://localhost:5000/todo1
# {"todo1": "Remember the milk"}
# $ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
# {"todo2": "Change my brakepads"}
# $ curl http://localhost:5000/todo2
# {"todo2": "Change my brakepads"}
#
# Flask-RESTful understands multiple kinds of return values from view methods.
#  Similar to Flask, you can return any iterable and it will be converted
#  into a response, including raw Flask response objects. Flask-RESTful
#   also support setting the response code and response headers using
#    multiple return values, as shown below:
#
#    class Todo1(Resource):
#     def get(self):
#         # Default to 200 OK
#         return {'task': 'Hello world'}
#
# class Todo2(Resource):
#     def get(self):
#         # Set the response code to 201
#         return {'task': 'Hello world'}, 201
#
# class Todo3(Resource):
#     def get(self):
#         # Set the response code to 201 and return custom headers
#         return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
