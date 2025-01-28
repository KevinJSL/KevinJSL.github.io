from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cp1', methods = ['GET', 'POST'])
def asnm1():
    return render_template("./cp1.html")

@app.route('/cp2', methods = ['GET', 'POST'])
def asnm2():
    return render_template("./cp2.html")

@app.route('/online_acts', methods = ['GET', 'POST'])
def oa():
    return render_template("./online_acts.html")


if __name__ == '__main__':
    app.run(debug=True)
