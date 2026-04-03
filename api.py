from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# কনফিগারেশন
TARGET_API = "https://devil-api.elementfx.com/api/tg-num.php?key=OWNBOT-JSCZUB&usersid="
CREDIT = "SB-SAKIB"
DEV_USER = "@sakib01994"
GROUP = "@publicgroup5s"

@app.route('/')
def home():
    usersid = request.args.get('usersid')
    
    # যদি প্যারামিটার না থাকে বা এপি ফেল হয়
    if not usersid:
        return jsonify({
            "status": False,
            "message": "API REQUEST FAILED!",
            "error": "Missing 'usersid' parameter.",
            "instruction": f"Contact our Developer {DEV_USER} for access.",
            "group": GROUP
        }), 400

    try:
        # মেইন এপি থেকে ডেটা আনা
        response = requests.get(f"{TARGET_API}{usersid}", timeout=10)
        data = response.json()

        if data.get("status") == True:
            # প্রিমিয়াম কাস্টম জেসন আউটপুট
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
                    "api": "SB-SAKIB ",
                    "credit": CREDIT,
                    "developer": DEV_USER,
                    "community": GROUP
                }
            })
        else:
            raise Exception("Invalid Response")

    except Exception:
        return jsonify({
            "status": False,
            "message": "API CONNECTION FAILED!",
            "error": "Internal Server Error or Expired Key.",
            "contact": f"Message {DEV_USER} to fix this issue.",
            "group": GROUP
        }), 500

# ভার্সেল হ্যান্ডলার
def handler(event, context):
    return app(event, context)
