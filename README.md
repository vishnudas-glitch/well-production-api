# 🛢️ Well Metrics API

A lightweight Flask-based REST API for retrieving well production data (OIL, GAS, BRINE) from a SQLite database. Features built-in Swagger docs, standardized responses, and robust error logging.

---

## 🚀 Features

- ✅ Flask-based REST API
- 📄 Swagger API docs using Flasgger
- 🧠 Pydantic models for structured responses
- 🗃️ SQLite database integration
- 📁 Modular project layout
- 📦 Environment config via .env
- 🔒 Logs only errors to a log file
- 🐳 Production-ready (gunicorn-friendly)

---

## 📁 Project Structure

```
├── scripts/
│   └── load_data.py
├── app/
│   ├── __init__.py             # App factory with logger and Swagger config
│   ├── config/
│   │   ├── settings.py         # Environment variable configs
│   │   └── db/
│   │       └── database.py     # DB connection and teardown logic
│   ├── routes/
│   │   ├── __init__.py         # Blueprint registration
│   │   ├── well_production.py  # Main route logic
│   │   └── swagger/
│   │       └── well_production.py  # Swagger docs per route
│   ├── services/
│   │   └── well_service.py     # Data fetching logic from DB
│   ├── helpers/
│   │   └── utils.py            # Standardized API response helper
│   └── models/
│       └── base.py             # OutModel for API responses
├── .env                        # Environment configuration
├── run.py                      # Entry point for local or gunicorn
└── requirements.txt            # Python dependencies
```

---

## 🔧 Setup

### 1. Clone the repo

```bash
git clone https://github.com/vishnudas-bluefox/well-production-api
cd well-production-api
```

### 2. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
DATABASE=ohio.db

DEBUG=False
LOG_LEVEL=ERROR
LOG_FILE_NAME=ohio_backend.log
PORT=8080
HOST=0.0.0.0

API_TITLE=Well Data API
API_DESCRIPTION=Get production data from SQLite
API_VERSION=1.0
```

### 4. Building the Database (Optional)

Before running the API, generate the `ohio.db` SQLite database by running the data loader script:

```bash
python3 scripts/load_data.py
```

This script reads from the raw data files and populates your local SQLite database for the API to serve.

---

## ▶️ Running the App

### Development (Flask)

```bash
python main.py
```

### Production (Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:8080 app:create_app
```

---

## 🧪 API Usage

**GET /data?well=1234567890**

Returns OIL, GAS, BRINE data for the requested API WELL NUMBER.

📄 Swagger UI:  
`http://localhost:8080/apidocs/`

---

## 📦 Response Format

```json
{
  "status": "success",
  "status_code": 200,
  "comment": "Well data retrieved successfully",
  "data": {
    "OIL": 862,
    "GAS": 230195,
    "BRINE": 2050
  }
}
```

---

## 📜 Logging

Logs only `ERROR` level and above to the file specified in `.env` (e.g. `ohio_backend.log`):

```bash
tail -f error.log
```

---
