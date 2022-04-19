class Controllers:
    @staticmethod
    def init_app(app):
        from .tmdb import tmdb_bp
        from .api import api_bp

        app.register_blueprint(api_bp)
        app.register_blueprint(tmdb_bp)
