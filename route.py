from flask import Flask, render_template, render_template_string

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    with open("index.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/cp1', methods = ['GET', 'POST'])
def asnm1():
    with open("./templates/cp1.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/cp2', methods = ['GET', 'POST'])
def asnm2():
    return render_template("./cp2.html")

@app.route('/online_acts', methods = ['GET', 'POST'])
def oa():
    return render_template("./online_acts.html")


if __name__ == '__main__':
    app.run(debug=True)
