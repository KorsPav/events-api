from .base import *

DEBUG = os.getenv('DEBUG') == '1'

INSTALLED_APPS += (
    'anymail',
)

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY')}
DEFAULT_FROM_EMAIL = f'Events.com <{os.getenv("DEFAULT_FROM_EMAIL")}>'
