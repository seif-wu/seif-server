class Schema:
    @staticmethod
    def init_app(app):
        from . import user_schema, wechat_user_schema, watched_schema, want_watch_schema
