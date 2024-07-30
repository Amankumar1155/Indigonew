from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import firebase_admin
from firebase_admin import messaging, credentials
from flight_status import get_flight_status

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flightStatusDB"
mongo = PyMongo(app)

# Initialize Firebase Admin
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
    # Example payload
    data = request.get_json()
    title = data.get('title', 'Flight Status Update')
    body = data.get('body', 'Your flight status has changed.')

    # Create a message object
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        topic='flight_updates'
    )

    try:

        response = messaging.send(message)
        return jsonify({"message_id": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
aman