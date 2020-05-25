

class Config:
    EXTRA_AMOUNT = 1.0
    REDIRECT_URL = "http://meusite.com/obrigado"
    NOTIFICATION_URL = "http://meusite.com/notification"
    EMAIL = "jefferson.ximenes11@hotmail.com"
    TOKEN = "55bce4ea-4840-42f1-9185-c048ef0cb17075d4b770411ea9ddf5d2cd76aa160854f5cf-3025-4f77-8c4e-277bd7865b52"
    SECRET_KEY = "tasafe"


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'


CONFIG = {
    'development': DevelopmentConfig
}
