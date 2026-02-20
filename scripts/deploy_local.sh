#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/opt/cicd-demo"

echo "[1/6] Sync code to ${APP_DIR}"
mkdir -p "${APP_DIR}"
rsync -a --delete \
  --exclude ".git" \
  --exclude ".venv" \
  --exclude "__pycache__" \
  ./ "${APP_DIR}/"

cd "${APP_DIR}"

echo "[2/6] Create venv if missing"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

echo "[3/6] Install dependencies"
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "[4/6] Restart service"
sudo systemctl restart cicd-demo

echo "[5/6] Health check"
curl -fsS http://127.0.0.1:5000/health || exit 1

echo "[6/6] Deployment complete"

