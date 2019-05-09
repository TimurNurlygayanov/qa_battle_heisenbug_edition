#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask import request
import hashlib
import requests


UPLOAD_FOLDER = '/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False
app.secret_key = str(hashlib.sha224('QA Battle Heisenbug'.encode('utf-8')
                                    ).hexdigest())


@app.route('/check', methods=['GET'])
def check():
    return flask.jsonify('OK')


@app.route('/auth', methods=['POST'])
def authorize():

    if request.method == 'POST':
        login_token = str(request.values['token'])

        url = 'http://ulogin.ru/token.php?token={0}&host={1}'
        res = requests.get(url.format(login_token, 'localhost'))

        try:
            data = res.json()

            user_name = str(data['email']).lower()

            with open('/users.txt', 'w+') as f:
                f.write('{0}\n'.format(user_name))

        except:
            pass

        return flask.redirect('/start_dream.html')

    return flask.jsonify('internal error: please write to Telegram @xwizard707 about the issue! Thank you!')


if __name__ == "__main__":
    app.run('0.0.0.0')