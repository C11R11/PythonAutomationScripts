from flask import Flask, jsonify, Response
from uuid import uuid4
from concurrent.futures import ThreadPoolExecutor
import time
import os
import gzip

app = Flask(__name__)

# Global variables used by the thread executor, and the thread executor itself
NUM_THREADS = 1
EXECUTOR = ThreadPoolExecutor(NUM_THREADS)
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# this is your long running processing function
# takes in your arguments from the /queue-task endpoint
def a_long_running_task(*args):
    time_to_wait, output_file_name = int(args[0][0]), args[0][1]
    output_string = 'sleeping for {0} seconds. File: {1}'.format(time_to_wait, output_file_name)
    print(output_string)
    time.sleep(time_to_wait)
    filename = os.path.join(OUTPUT_DIR, output_file_name)
    # here we are writing to a gzipped file to save space and decrease size of file to be sent on network
    with gzip.open(filename, 'wb') as f:
        f.write(output_string)
    print('finished writing {0} after {1} seconds'.format(output_file_name, time_to_wait))

# This is a route that starts the task and then gives them the file name for reference
@app.route('/queue-task/<wait>')
def queue_task(wait):
    output_file_name = str(uuid4()) + '.csv'
    EXECUTOR.submit(a_long_running_task, [wait, output_file_name])
    return jsonify({'filename': output_file_name})

# this takes the file name and returns if exists, otherwise notifies it is not yet done
@app.route('/getfile/<name>')
def get_output_file(name):
    file_name = os.path.join(OUTPUT_DIR, name)
    print(file_name)
    if not os.path.isfile(file_name):
        return jsonify({"message": "still processing"})
    # read without gzip.open to keep it compressed
    with open(file_name, 'rb') as f:
        resp = Response(f.read())
    # set headers to tell encoding and to send as an attachment
    resp.headers["Content-Encoding"] = 'gzip'
    resp.headers["Content-Disposition"] = "attachment; filename={0}".format(name)
    resp.headers["Content-type"] = "text/csv"
    return resp


if __name__ == '__main__':
    app.run()
