from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "HelloWorld!"

@app.route("/Example")
def example():
    return "HelloExample!"

if __name__ == "__main__":
    app.run(debug=True)
