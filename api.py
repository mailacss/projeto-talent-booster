from flask import Flask, json, jsonify, render_template

import question02 as q2
import question03 as q3
import question04 as q4
import question06 as q6
import question07 as q7
import question08 as q8

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/question02")
def ques2():
    return q2.item2()

@app.route("/question03")
def ques3():
    return q3.item3()

@app.route("/question04")
def ques4():
    return q4.resultado04

@app.route("/question06")
def ques6():
    return q6.item6()

@app.route("/question07")
def ques7():
    return q7.item7()

@app.route("/question08")
def ques8():
    return q8.item8()

if __name__ == "__main__":
    app.run(debug=True)