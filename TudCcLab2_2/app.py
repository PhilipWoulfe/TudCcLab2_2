"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import jsonify
import subprocess
from subprocess import Popen
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/status')
def status():
    """Renders a sample page."""
    out_dict = {}
    out_dict["hostname"] = run_cmd(["hostname"])
    out_dict["ip_address"] = os.environ.get('SERVER_HOST', 'localhost')
    out_dict["cpus"] = os.environ.get('SERVER_HOST', 'localhost')
    out_dict["memory"] = os.environ.get('SERVER_HOST', 'localhost')
    return jsonify(out_dict)

def run_cmd(commands):
    result = subprocess.run(commands, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').rstrip();

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
