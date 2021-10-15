from flask import Flask, json, jsonify, render_template
import question08 as q8

app = Flask(__name__)

@app.route("/question08")
def ques8():
    return q8.item8()

if __name__ == "__main__":
    app.run(debug=True)