from flask import Flask

def create_ap():
    app = Flask(__name__)
    app.config['SECREY_KEY'] = 'dknfldsnfank skdnfodnoos'


    return app