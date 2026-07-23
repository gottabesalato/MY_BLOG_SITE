import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Look for real email settings first. If you don't find them, use our local aiosmtpd testing loop.
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or '127.0.0.1'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-example@gmail.com']

    # Post per page configuration
    POSTS_PER_PAGE = 3 ##REMEMBER TO CHANGE THIS NUMBER IN FUTURE

