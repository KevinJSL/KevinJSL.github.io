from flask import Blueprint, render_template

animation_bp = Blueprint('animation', __name__)

@animation_bp.route('/a/')
def animation():
    return render_template('animation/animation.html')

@animation_bp.route('/a0/')
def a0():
    return render_template('animation/a0.html')

@animation_bp.route('/a1/')
def a1():
    return render_template('animation/a1.html')

@animation_bp.route('/a2/')
def a2():
    return render_template('animation/a2.html')

@animation_bp.route('/a3/')
def a3():
    return render_template('animation/a3.html')

@animation_bp.route('/a4/')
def a4():
    return render_template('animation/a4.html')