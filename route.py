from flask import Flask, render_template_string, render_template

app = Flask(__name__, static_url_path='/static')


# Index
@app.route('/')
def index():
    return render_template("index.html")

# School
@app.route('/sw')
def school_work():
    return render_template('school-work.html')

# Animation
@app.route('/a')
def animation():
    return render_template('animation/animation.html')

@app.route('/a0')
def a_a0():
    return render_template('animation/a0.html')

# Global Illumination
@app.route('/gi')
def global_illumination():
    return render_template('global_illumination/global_illumination.html')

@app.route('/cp1')
def asnm1():
    return render_template('global_illumination/cp1.html')

@app.route('/cp2')
def asnm2():
    return render_template('global_illumination/cp2.html')

@app.route('/cp3')
def asnm3():
    return render_template('global_illumination/cp3.html')

@app.route('/cp4')
def asnm4():
    return render_template('global_illumination/cp4.html')

@app.route('/cp5')
def asnm5():
    return render_template('global_illumination/cp5.html')

@app.route('/cp6')
def asnm6():
    return render_template('global_illumination/cp6.html')

@app.route('/cp7')
def asnm7():
    return render_template('global_illumination/cp7.html')

@app.route('/KD')
def assmKD():
    return render_template('global_illumination/KD.html')

@app.route('/volume')
def assmFinal():
    return render_template('global_illumination/volume.html')

# Projects
@app.route('/pp')
def projects():
    return render_template('personal-projects.html')

# Papers
@app.route('/p')
def papers():
    return render_template('publications.html')


if __name__ == '__main__':
    app.run(debug=True)
