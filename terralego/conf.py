import os


class Settings(object):

    TERRALEGO_URL = os.getenv('TERRALEGO_URL', 'https://terralego.fr/{api}/')
    USER = os.getenv('TERRALEGO_USER', None)
    PASSWORD = os.getenv('TERRALEGO_PASSWORD', None)

settings = Settings()
