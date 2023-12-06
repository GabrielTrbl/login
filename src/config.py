class Config:
    SECRET_KEY = 'Hola'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'Gabriel45.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'Gabriel45'
    MYSQL_PASSWORD = 'Basecita37'
    MYSQL_DB = 'Gabriel45$MusicPage'

config={
    'development': DevelopmentConfig
}