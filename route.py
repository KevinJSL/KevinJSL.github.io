from flask import Flask, render_template
from flask_frozen import Freezer   # <-- NEW

app = Flask(__name__, static_url_path='/static')
freezer = Freezer(app)             # <-- NEW

# ---------- ROUTES ----------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sw/')
def school_work():
    return render_template('school-work.html')

@app.route('/a/')
def animation():
    return render_template('animation/animation.html')

@app.route('/a0/')
def a_a0():
    return render_template('animation/a0.html')

@app.route('/gi/')
def global_illumination():
    return render_template('global_illumination/global_illumination.html')

@app.route('/cp1/')
def asnm1():
    return render_template('global_illumination/cp1.html')

@app.route('/cp2/')
def asnm2():
    return render_template('global_illumination/cp2.html')

@app.route('/cp3/')
def asnm3():
    return render_template('global_illumination/cp3.html')

@app.route('/cp4/')
def asnm4():
    return render_template('global_illumination/cp4.html')

@app.route('/cp5/')
def asnm5():
    return render_template('global_illumination/cp5.html')

@app.route('/cp6/')
def asnm6():
    return render_template('global_illumination/cp6.html')

@app.route('/cp7/')
def asnm7():
    return render_template('global_illumination/cp7.html')

@app.route('/KD/')
def assmKD():
    return render_template('global_illumination/KD.html')

@app.route('/volume/')
def assmFinal():
    return render_template('global_illumination/volume.html')

@app.route('/pp/')
def projects():
    return render_template('personal-projects.html')

@app.route('/p/')
def papers():
    return render_template('publications.html')

# ---------- MAIN ----------
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()   # <-- NEW: generate static site into ./build/
    else:
        app.run(debug=True)
