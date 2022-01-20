from flask import Flask

app = Flask(__name__)

# index page
@app.route("/")
def Hello():
    return "Hello, This is Basic flask app"

# Input name parameter
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}, Welcome to flask app"


if __name__ == "__main__":
    app.run(debug=True)