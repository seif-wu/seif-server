class Controllers:
    @staticmethod
    def init_app(app):
        from .api.tmdb import tmdb_bp

        app.register_blueprint(tmdb_bp)
