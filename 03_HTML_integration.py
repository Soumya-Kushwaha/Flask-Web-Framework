# Integrate HTML with Flask

## HTTP verb GET and POST

# Building URL Dynamically

## Variable Rules and URL Building

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', result = res)


@app.route('/failure/<int:score>')
def failure(score):
    return "The person has failed and has" + str(score) + " marks."


@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks >= 50:
        result = "success"
    else:
        result = "failure"
    return redirect(url_for(result, score=marks))


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science)/4
    res = ""
    return redirect(url_for('success', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)
