from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World, from Flask!"

@app.route("/test/")
def test():
    return "test test test"


if __name__ == "__main__":
    app.run()