from flask import Flask, jsonify
import os
from datetime import datetime, timezone

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "CI/CD Demo Service")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
GIT_SHA = os.getenv("GIT_SHA", "local")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

@app.get("/")
def home():
    return (
        f"<h2>{APP_NAME}</h2>"
        f"<p>Environment: <b>{ENVIRONMENT}</b></p>"
        f"<p>Version: <b>{APP_VERSION}</b></p>"
        f"<p>Commit: <b>{GIT_SHA}</b></p>"
    )

@app.get("/health")
def health():
    return jsonify(
        status="running",
        environment=ENVIRONMENT,
        version=APP_VERSION,
        git_sha=GIT_SHA,
        timestamp=datetime.now(timezone.utc).isoformat()
    )

@app.get("/version")
def version():
    return jsonify(
        app=APP_NAME,
        version=APP_VERSION,
        git_sha=GIT_SHA
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
