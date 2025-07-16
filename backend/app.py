from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Default root route
@app.route('/')
def home():
    return "🚗 AutoScaleDrive Flask API is running!"

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('AutoScaleDriveResults')

@app.route('/decide-mode', methods=['POST'])
def decide_mode():
    data = request.get_json()
    print(f"Received data: {data}")

    temp = data.get('engine_temp')
    sound = data.get('engine_sound')
    tyre = data.get('tyre_pressure')
    fuel = data.get('fuel_level')
    climate = data.get('climate')

    reason = ""
    mode = "Normal"

    if temp is None or sound is None or tyre is None or fuel is None or climate is None:
        return jsonify({"error": "Missing required inputs"}), 400

    if temp > 120:
        mode = "Safety"
        reason = "Extreme engine heat detected. Switching to Safety mode."
    elif climate == "rain" and temp < 40:
        mode = "Safety"
        reason = "Rainy climate with cold engine. Need warm-up."
    elif climate == "rain" and tyre < 24:
        mode = "Safety"
        reason = "Rainy weather with low tyre pressure. Risk of slipping."
    elif fuel < 30:
        mode = "Eco"
        reason = "Low fuel. Eco mode activated for efficiency."
    elif fuel > 70 and climate == "sun" and temp < 100:
        mode = "Sport"
        reason = "Good conditions and full fuel. Activating Sport mode."
    else:
        mode = "Normal"
        reason = "Conditions stable. Default Normal mode applied."

    item = {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.utcnow().isoformat(),
        'inputs': data,
        'mode': mode,
        'reason': reason
    }

    try:
        table.put_item(Item=item)
        print("Saved to DynamoDB successfully")
    except Exception as e:
        print(f"Error saving to DynamoDB: {e}")

    return jsonify({
        "mode": mode,
        "reason": reason,
        "inputs": data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
