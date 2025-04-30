from flask import Flask, render_template_string

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    with open("index.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp1', methods=['GET', 'POST'])
def asnm1():
    with open("cp1.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp2', methods=['GET', 'POST'])
def asnm2():
    with open("cp2.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp3', methods=['GET', 'POST'])
def asnm3():
    with open("cp3.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp4', methods=['GET', 'POST'])
def assm4():
    with open("cp4.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp5', methods=['GET', 'POST'])
def assm5():
    with open("cp5.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp6', methods=['GET', 'POST'])
def assm6():
    with open("cp6.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/cp7', methods=['GET', 'POST'])
def assm7():
    with open("cp7.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/KD', methods=['GET', 'POST'])
def assmKD():
    with open("KD.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


@app.route('/volume', methods=['GET', 'POST'])
def assmFinal():
    with open("volume.html", "r") as f:
        html_content = f.read()
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)
