from flask import Flask
from flask import request
import subprocess
app = Flask(__name__)

task_list = []
cmd_output = {}
index_counter = 0

@app.route('/')
def hello_world():
    return 'Hello, World! This is fun with flags'

@app.route('/cmd', methods = ['POST'])
def run_command_and_store_output_and_command():
    global task_list
    global cmd_output
    global index_counter
    index_counter += 1
    task_list = task_list + [request.json['command']]
    print(str(task_list) + '\n')
    cmd = request.json['command'].split()
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    cmd_output[index_counter] = out
    print(str(cmd_output) + '\n')
    return 'Task id:' + str(index_counter) + '\n'

@app.route('/tasklist', methods = ['GET'])
def list_tasks():
    return str(task_list)

@app.route('/spectask/<id>', methods = ['GET'])
def specific_task(id):
    print(id)
    return str(cmd_output[int(id)])
