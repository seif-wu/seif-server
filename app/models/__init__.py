class Models:
    @staticmethod
    def init_app(app):
        from . import user, \
                wechat_mini_program, \
                wechat_user, \
                watched, \
                want_watch, \
                personal_information, \
                work_history, \
                project_history
