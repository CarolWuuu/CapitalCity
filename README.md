# CapitalCity

A simple Flask API that returns the current local time and UTC offset for a given capital city. Includes token-based authentication.
Supported Capital Cities
- Washington
- London
- Tokyo
- Paris
- Beijing
- New Delhi
- Canberra
- Ottawa
- Brasília
  
## Live API URL

`http://34.134.73.118:5000/api/time`

## Token Authentication

This API requires a token for access. Include the following header in your request:
Authorization: Bearer supersecrettoken123

**Example:**
```bash
curl -H "Authorization: Bearer supersecrettoken123" \
"http://34.134.73.118:5000/api/time?capital=London"

**Response:**
{
  "capital": "London",
  "local_time": "2025-04-15 20:40:00",
  "utc_offset": "+01:00"
}

## Set up instruction
1. clone repo:
git clone https://github.com/CarolWUuu/CapitalCity.git
cd CapitalCity

2. Set up Python virtual environment (on GCP)
python3 -m venv flask-env
source flask-env/bin/activate
pip install -r requirements.txt

3. run the app:
python app.py



