#!/usr/bin/python3

from flask import request, Flask, render_template
import subprocess
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'host' not in request.form:
            return "WUUUUUUUUT???"

        host = request.form['host']
        if '$' in host or '(' in host or '[' in host or '{' in host or '\\' in host:
            return "GET OUT WITH THOSE NAUGHTY CHARS SCRIPT KIDDY!!!"

        try:
            subprocess.run("ping -c 1 -W 1 " + host, shell=True, check=True, capture_output=True)
            return render_template('page.html', message="Ping succeeded")
        except subprocess.CalledProcessError as e:
            msg = e.stderr.decode("utf-8")
            if len(msg) > 5:
                msg = msg[5:]
            return render_template('page.html', message="Ping failed " + msg)
    else:
        return render_template('page.html', message="")


if __name__ == '__main__':
    app.run(threaded=True)
