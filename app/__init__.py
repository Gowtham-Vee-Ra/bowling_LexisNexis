from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from app.controllers.game_controller import game_bp
    from app.controllers.player_controller import player_bp

    app.register_blueprint(game_bp, url_prefix='/games')
    app.register_blueprint(player_bp, url_prefix='/players')

    return app
