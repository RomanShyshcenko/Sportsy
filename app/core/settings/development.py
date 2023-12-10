import os
from .base import Base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Base):
    DEBUG = True
    # Set up testing settings
    INSTALLED_APPS = Base.INSTALLED_APPS
    # INSTALLED_APPS += ('django_nose',)
    #
    # TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    CORS_ORIGIN_WHITELIST = [
        "http://localhost:3000"
    ]
