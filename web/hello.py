import os
import socket
import datetime
from flask import Flask, request, render_template
import pymongo

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    try:
        server_hostname = socket.gethostname()
        date = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=1)))
        
        client_ip = request.remote_addr
        
        MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://admin:securepassword@localhost:27017/')
        client = pymongo.MongoClient(MONGO_URI)
        db = client["database_de_narcisse"]
        collection = db["collection_de_narcisse"]
        
        # Insert the new record
        collection.insert_one({"client_ip": client_ip, "date": date})
        
        # Retrieve the last 10 records
        records = list(collection.find().sort("_id", -1).limit(10))
        
        return render_template('index.html', dt=date, serv_host=server_hostname, records=records)
    except pymongo.errors.PyMongoError as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5066))
    app.run(debug=True, host='0.0.0.0', port=port)