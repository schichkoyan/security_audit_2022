import flask
from logging.config import dictConfig

from jinja_markdown import MarkdownExtension
import flask_httpauth
from flask_sqlalchemy import SQLAlchemy

# Logging Handler
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers':
    {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': '/tmp/logging.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
    }
})


app = flask.Flask(__name__)
app.secret_key = "Sup3r_SeKret_T0ken"
app.config.update(
    SESSION_COOKIE_SAMESITE='Strict',
    SQLALCHEMY_DATABASE_URI= 'sqlite:////tmp/test.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
)


app.jinja_env.add_extension(MarkdownExtension)


auth = flask_httpauth.HTTPBasicAuth()
bauth = flask_httpauth.HTTPTokenAuth()




        
