# coding: utf-8

from flask import Flask, session, url_for, request, jsonify
from flask_oauthlib.client import OAuth


app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'

# TODO: fill them
CLIENT_KEY = 'uwXf342HbsOrkeboDbWx4OP4FgP6MRgyFsVzEtJg'
CLIENT_SECRET = 'yd2YMidJfa6gtSyGyGDop9cf0uEFVRCkq9l3w3krFMZEG6kLop'

oauth = OAuth(app)
remote = oauth.remote_app(
    'remote',
    consumer_key=CLIENT_KEY,
    consumer_secret=CLIENT_SECRET,
    base_url='http://127.0.0.1:5000/api/',
    request_token_url='http://127.0.0.1:5000/oauth/request_token',
    access_token_method='GET',
    access_token_url='http://127.0.0.1:5000/oauth/access_token',
    authorize_url='http://127.0.0.1:5000/oauth/authorize',
)


@app.route('/')
def home():
    if 'example_oauth' in session:
        return session['example_oauth']
    return remote.authorize(callback=url_for('authorized', _external=True))


@app.route('/authorized')
@remote.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: error=%s' % (
            request.args['error']
        )
    if 'oauth_token' in resp:
        session['dev_oauth'] = resp
        return jsonify(resp)
    return str(resp)


import logging
logger = logging.getLogger('flask_oauthlib')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    app.run(host='localhost', port=8000)