from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import firebase_admin
from firebase_admin import messaging, credentials
from flight_status import get_flight_status

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flightStatusDB"
mongo = PyMongo(app)

cred = credentials.Certificate("path/to/firebase_credentials.json")
firebase_admin.initialize_app(cred)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status/<flight_id>')
def flight_status(flight_id):
    status = get_flight_status(flight_id)
    if status:
        return jsonify(status)
    else:
        return jsonify({"error": "Flight not found"}), 404

@app.route('/api/notify', methods=['POST'])
def notify():
    message = messaging.Message(
        notification=messaging.Notification(
            title='Flight Status Update',
            body='Your flight status has changed.'
        ),
        topic='flight_updates'
    )
    response = messaging.send(message)
    return jsonify({"message_id": response})

if __name__ == '__main__':
    app.run(debug=True)
