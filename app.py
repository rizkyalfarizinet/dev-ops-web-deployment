
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/api/status")
def status():
    return jsonify({
        "project": "DevOps Web Deployment",
        "status": "running",
        "technology": [
            "Python",
            "Flask",
            "Ubuntu Server"
        ],
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
