from flask import Blueprint, render_template

q_bp = Blueprint('quantum', __name__)

@q_bp.route('/q/')
def quantum_main():
    return render_template('quantum/quantum.html')