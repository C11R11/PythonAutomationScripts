from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class SolotodoStats(Resource):
    def get(self):
        r = requests.get('https://www.solotodo.com/', allow_redirects=True)
        resource_fields =   {   'status': r.status_code,
                                'holi'  : "holi"
                            }
        return resource_fields

api.add_resource(SolotodoStats, '/api/V1/solotodo/')

if __name__ == '__main__':
    app.run(debug=True)
