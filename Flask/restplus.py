"""
A mix of:
https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f
https://medium.com/ki-labs-engineering/designing-well-structured-rest-apis-with-flask-restplus-part-1-7e96f2da8850
"""

from flask import Flask
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(app = flask_app,
          version = "1.0",
		  title = "Test API",
		  description = "This is a test created by me")

name_space = app.namespace('okey', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

@name_space.route("/test")
class Test(Resource):
	def get(self):
		return {
			"status": "Test get"
		}
	def post(self):
		return {
			"status": "Test post"
		}
