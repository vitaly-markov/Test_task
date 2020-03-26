import flask
import socket
import sys
import os
import platform
from settings import fname

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    try:
        osname = platform.linux_distribution()
        platos = platform.system()
        relos = platform.release()
        kernal = platform.version()
        stname = fname['name'] + fname['surname']

        return render_template('index.html', ro=relos, on=osname[0], po=platos, k=kernal, sn=stname)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
