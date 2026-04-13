from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Config
TARGET_API = "https://devil-api.elementfx.com/api/tg-num.php?key=OWNBOT-JSCZUB&usersid="
CREDIT = "SB-SAKIB"
DEV_USER = "@sakib01994"
GROUP = "@publicgroup5s"

@app.route('/')
def home():
    usersid = request.args.get('usersid')
    
    # parameter missing handling
    if not usersid:
        return jsonify({
            "status": False,
            "message": "API REQUEST FAILED!",
            "contact": f"Contact Developer {DEV_USER}",
            "group": GROU
        }), 400

    try:
        response = requests.get(f"{TARGET_API}{usersid}", timeout=10)
        data = response.json()

        if data.get("status") == True:
            res = data["results"]["result"]
            return jsonify({
                "status": True,
                "results": {
                    "success": True,
                    "query": usersid,
                    "result": {
                        "country": res.get("country", "Unknown"),
                        "country_code": res.get("country_code", "N/A"),
                        "number": res.get("number", "Not Found"),
                        "msg": "Details fetched successfully"
                    }
                },
                "branding": {
                    "api": "SB-SAKIB",
                    "credit": CREDIT,
                    "developer": DEV_USER,
                    "community": GROUP
                }
            })
        else:
            return jsonify({
                "status": False,
                "message": "API FAILED! User Not Found or Key Expired.",
                "contact": DEV_USER
            }), 404

    except Exception:
        return jsonify({
            "status": False,
            "message": "CONNECTION ERROR!",
            "contact": f"Message {DEV_USER} to fix."
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
