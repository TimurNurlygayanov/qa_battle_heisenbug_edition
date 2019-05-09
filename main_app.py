#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask import request
import hashlib
import requests
import codecs


UPLOAD_FOLDER = '/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False
app.secret_key = str(hashlib.sha224('QA Battle Heisenbug'.encode('utf-8')
                                    ).hexdigest())


@app.route('/auth/check', methods=['GET'])
def check():
    return flask.jsonify('OK')


@app.route('/auth/auth', methods=['POST'])
def authorize():

    if request.method == 'POST':
        login_token = str(request.values['token'])

        url = 'http://ulogin.ru/token.php?token={0}&host={1}'
        res = requests.get(url.format(login_token, 'localhost'))

        data = res.json()

        with codecs.open('/users.txt', 'w+', 'utf-8') as f:
            f.write('@@@ {0} {1} - {2} ###\n'.format(data['first_name'],
                                                     data['last_name'],
                                                     data['email']))

        return flask.redirect('/start_dream.html')

    return flask.jsonify('internal error: please write to Telegram @xwizard707 about the issue! Thank you!')


if __name__ == "__main__":
    app.run('0.0.0.0')
