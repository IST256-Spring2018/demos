from flask import Flask, render_template, request
app = Flask(__name__)
import json

@app.route("/")
def main():
    return json.dumps({"name": "ist256"})

if __name__ == "__main__":
    app.run(debug=True)