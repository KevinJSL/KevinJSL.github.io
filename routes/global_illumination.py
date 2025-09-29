from flask import Blueprint, render_template

gi_bp = Blueprint('global_illumination', __name__)

@gi_bp.route('/gi/')
def global_illumination():
    return render_template('global_illumination/global_illumination.html')

@gi_bp.route('/cp1/')
def asnm1():
    return render_template('global_illumination/cp1.html')

@gi_bp.route('/cp2/')
def asnm2():
    return render_template('global_illumination/cp2.html')

@gi_bp.route('/cp3/')
def asnm3():
    return render_template('global_illumination/cp3.html')

@gi_bp.route('/cp4/')
def asnm4():
    return render_template('global_illumination/cp4.html')

@gi_bp.route('/cp5/')
def asnm5():
    return render_template('global_illumination/cp5.html')

@gi_bp.route('/cp6/')
def asnm6():
    return render_template('global_illumination/cp6.html')

@gi_bp.route('/cp7/')
def asnm7():
    return render_template('global_illumination/cp7.html')

@gi_bp.route('/KD/')
def assmKD():
    return render_template('global_illumination/KD.html')

@gi_bp.route('/volume/')
def assmFinal():
    return render_template('global_illumination/volume.html')
