import time
from flask import Flask
from flask import Response


app = Flask(__name__)


def random():
    while True:
        time.sleep(1)
        yield(
            '''--bytes\r\n
            Content-Disposition: x-www-form-urlencoded\r\n\r\n
            msg=Hello World!&age=13
            \r\n''')

@app.route("/")
def hello_world():
    return Response(random(), mimetype='multipart/form-data; boundary=bytes')
