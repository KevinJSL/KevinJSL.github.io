from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template("index.html")

@main_bp.route('/sw/')
def school_work():
    return render_template('school-work.html')

@main_bp.route('/pp/')
def projects():
    return render_template('personal-projects.html')

@main_bp.route('/p/')
def papers():
    return render_template('publications.html')
