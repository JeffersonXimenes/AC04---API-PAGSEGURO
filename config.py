

class Config:
    EXTRA_AMOUNT = 1.0
    REDIRECT_URL = "http://meusite.com/obrigado"
    NOTIFICATION_URL = "http://meusite.com/notification"
    EMAIL = "seuemail@teste.com"
    TOKEN = "token que eu citei no vídeo"
    SECRET_KEY = "sua chave secreta"


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'


CONFIG = {
    'development': DevelopmentConfig
}
