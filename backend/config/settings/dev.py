from .base import *

DEBUG = True


# MailTrap settings:
EMAIL_HOST = os.getenv('MAILTRAP_EMAIL_HOST', 'smtp.mailtrap.io')
EMAIL_PORT = os.getenv('MAILTRAP_EMAIL_PORT', '2525')
EMAIL_HOST_USER = os.getenv('MAILTRAP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('MAILTRAP_EMAIL_HOST_PASSWORD')
