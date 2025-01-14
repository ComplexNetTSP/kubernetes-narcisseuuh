import os
import socket
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    server_hostname = socket.gethostname()
    date = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=1)))
    return render_template('index.html', dt=date, serv_host=server_hostname)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5067))
    app.run(debug=True, host='0.0.0.0', port=port)