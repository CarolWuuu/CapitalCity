from flask import Flask, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"  # Use env vars in real apps

# Dictionary of capital cities and their time zones
capital_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Beijing": "Asia/Shanghai",
    "New Delhi": "Asia/Kolkata",
    "Canberra": "Australia/Sydney",
    "Ottawa": "America/Toronto",
    "Brasília": "America/Sao_Paulo"
}

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    capital = request.args.get('capital')

    if not capital:
        return jsonify({"error": "Capital parameter is missing"}), 400

    timezone = capital_timezones.get(capital)
    if not timezone:
        return jsonify({"error": f"'{capital}' not found in database."}), 404

    tz = pytz.timezone(timezone)
    local_time = datetime.now(tz)
    offset = local_time.strftime('%z')
    offset_hours = f"{offset[:3]}:{offset[3:]}"  # format +0530 to +05:30

    return jsonify({
        "capital": capital,
        "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": offset_hours
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
