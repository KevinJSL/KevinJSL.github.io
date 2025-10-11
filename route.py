from flask import Flask
from flask_frozen import Freezer
from routes.main import main_bp
from routes.animation import animation_bp
from routes.global_illumination import gi_bp

def create_app(is_build=False):
    app = Flask(__name__, static_url_path='/static')

    # Common config
    app.config['APPLICATION_ROOT'] = '/'
    app.config['PREFERRED_URL_SCHEME'] = 'http'

    # Only set SERVER_NAME when building static site
    if is_build:
        app.config['SERVER_NAME'] = 'localhost:5000'

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(animation_bp)
    app.register_blueprint(gi_bp)

    return app


# ---------- MAIN ----------
if __name__ == '__main__':
    import sys

    # Detect if user passed "build" argument
    is_build = len(sys.argv) > 1 and sys.argv[1] == "build"

    app = create_app(is_build)
    freezer = Freezer(app)

    if is_build:
        print("🔧 Freezing site into ./build/ ...")
        freezer.freeze()
        print("✅ Static site built successfully!")
    else:
        print("🚀 Running Flask development server...")
        app.run(debug=True)
