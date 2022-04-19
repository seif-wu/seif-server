import os


class Config:
    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("APP_SECRET_KEY")
    JSON_AS_ASCII = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    @staticmethod
    def init_app(app):
        pass

# 数据库
mysql_username=os.getenv("MYSQL_USERNAME")
mysql_password=os.getenv("MYSQL_PASSWORD")
mysql_server=os.getenv("MYSQL_SERVER")
mysql_db_name=os.getenv("MYSQL_DB_NAME")
mysql_port=os.getenv("MYSQL_PORT")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_server}:{mysql_port}/{mysql_db_name}_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_server}:{mysql_port}/{mysql_db_name}_test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_server}:{mysql_port}/{mysql_db_name}'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
