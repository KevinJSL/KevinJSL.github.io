from flask import Flask
from flask_frozen import Freezer
from routes.main import main_bp
from routes.animation import animation_bp
from routes.global_illumination import gi_bp

def create_app():
    app = Flask(__name__, static_url_path='/static')
    
    # Configure for URL building outside request context
    app.config['SERVER_NAME'] = 'localhost:5000'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(animation_bp)
    app.register_blueprint(gi_bp)
    
    return app

app = create_app()
freezer = Freezer(app)

# ---------- MAIN ----------
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()   # <-- NEW: generate static site into ./build/
    else:
        app.run(debug=True)
