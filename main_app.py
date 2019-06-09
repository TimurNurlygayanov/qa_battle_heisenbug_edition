#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask import request
import hashlib
import requests
import codecs

from uuid import uuid4
import subprocess


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

        with codecs.open('/users.txt', 'a+', 'utf-8') as f:
            f.write(data['first_name'] + ' ' + data['last_name'] +
                    ' with email: ' + data['email'] + '\n')

        return flask.redirect('/start_dream.html')

    return flask.jsonify('internal error: please write to Telegram @xwizard707 about the issue! Thank you!')


@app.route('/auth/run_code', methods=['POST'])
def execute_task():

    docker_run_cmd_python3 = ('docker run --read-only -v '
                              '/tmp/{0}.py:/app/main.py python3 main.py')

    if request.method == 'POST':
        code = str(request.values['source_code'])
        worker_id = str(uuid4())

        with open('/tmp/{0}.py'.format(worker_id), 'w') as f:
            f.write(code)

        result = subprocess.run(docker_run_cmd_python3.format(worker_id),
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT).stdout.read()
        # except:
        #     result = 'Timeout: 10 seconds'  # this is for timeout handling

        return flask.jsonify({'result': result})


if __name__ == "__main__":
    app.run('0.0.0.0', threaded=True)
