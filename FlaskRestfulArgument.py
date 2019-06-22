#Argument Parsing
# While Flask provides easy access to request data (i.e. querystring or POST form encoded data), it’s still a pain to validate form data. Flask-RESTful has built-in support for request data validation using a library similar to argparse.
#
# from flask_restful import reqparse
#
# parser = reqparse.RequestParser()
# parser.add_argument('rate', type=int, help='Rate to charge for this resource')
# args = parser.parse_args()
# Note
# Unlike the argparse module, reqparse.RequestParser.parse_args() returns a Python dictionary instead of a custom data structure.
#
# Using the reqparse module also gives you sane error messages for free. If an argument fails to pass validation, Flask-RESTful will respond with a 400 Bad Request and a response highlighting the error.
#
# $ curl -d 'rate=foo' http://127.0.0.1:5000/todos
# {'status': 400, 'message': 'foo cannot be converted to int'}
# The inputs module provides a number of included common conversion functions such as inputs.date() and inputs.url().
#
# Calling parse_args with strict=True ensures that an error is thrown if the request includes arguments your parser does not define.
#
# args = parser.parse_args(strict=True)
