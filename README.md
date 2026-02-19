# CI/CD Pipeline (GitHub Actions)

A small production-style Flask service used to demonstrate CI/CD fundamentals:
- Automated testing on every push
- Build metadata injected via pipeline variables
- Clean endpoints used in real systems (`/health`, `/version`)

## Endpoints
- `GET /` – service landing page
- `GET /health` – health check + runtime metadata
- `GET /version` – version + commit SHA

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py

Open:

http://localhost:5000/health

http://localhost:5000/version


