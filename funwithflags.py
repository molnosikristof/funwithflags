from flask import Flask
from flask import request
import subprocess
app = Flask(__name__)

task_list = []

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/resource', methods = ['POST'])
def post_methods():
    global task_list
    task_list = task_list + [request.json['command']]
    return str(task_list) + '\n'
@app.route('/cmd', methods = ['POST'])
def run_command_and_store_output_and_command():
    global task_list
    task_list = task_list + [request.json['command']]
    print(str(task_list) + '\n')
    cmd = request.json['command'].split()
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return str(task_list) + '\n'
