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


@app.route('/auth/check', methods=['GET'])
def check():
    return flask.jsonify('OK')


@app.route('/auth/auth', methods=['POST'])
def authorize():

    if request.method == 'POST':
        login_token = str(request.values['token'])

        url = 'http://ulogin.ru/token.php?token={0}&host={1}'
        res = requests.get(url.format(login_token, 'localhost'))

        try:
            data = res.json()

            user_name = u'{0}'.format(data['first_name'] + data['last_name'])
            user_email = u'{0}'.format(data['email'])

            with open('/users.txt', 'w+') as f:
                f.write('@@@ {0} - {1} ###\n'.format(user_name, user_email.lower()))

        except Exception as e:
            with open('/qabattle.log', 'w+') as f:
                f.write(res.text)
                f.write(str(e))

        return flask.redirect('/start_dream.html')

    return flask.jsonify('internal error: please write to Telegram @xwizard707 about the issue! Thank you!')


if __name__ == "__main__":
    app.run('0.0.0.0')