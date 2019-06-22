# Data Formatting
# By default, all fields in your return iterable will be rendered as-is.
# While this works great when you’re just dealing with Python data structures,
#  it can become very frustrating when working with objects.
#  To solve this problem, Flask-RESTful provides the fields module and
#  the marshal_with() decorator. Similar to the Django ORM and WTForm,
#   you use the fields module to describe the structure of your response.
#
# from flask_restful import fields, marshal_with
#
# resource_fields = {
#     'task':   fields.String,
#     'uri':    fields.Url('todo_ep')
# }
#
# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task
#
#         # This field will not be sent in the response
#         self.status = 'active'
#
# class Todo(Resource):
#     @marshal_with(resource_fields)
#     def get(self, **kwargs):
#         return TodoDao(todo_id='my_todo', task='Remember the milk')
#
# The above example takes a python object and prepares it to be serialized.
#  The marshal_with() decorator will apply the transformation described by
#  resource_fields. The only field extracted from the object is task. The
#  fields.Url field is a special field that takes an endpoint name and
#   generates a URL for that endpoint in the response. Many of the field
# types you need are already included. See the fields guide for a complete
# list.
