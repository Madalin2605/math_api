# Math API Microservice

A lightweight Python microservice that exposes a RESTful API to perform basic mathematical operations:

- Power function (`base ^ exponent`)
- N-th Fibonacci number
- Factorial of a number

Each request is validated using Pydantic, logged into a SQLite database, and can also be triggered via a minimal HTML interface.

---

## Project Structure

```
math_api/
├── app/
│   ├── controllers/          # Business logic layer
│   ├── models/               # SQLAlchemy DB models
│   ├── routes/               # API + Web route handlers (Flask Blueprints)
│   ├── schemas/              # Pydantic models for request/response validation
│   ├── utils/                # Core math operations
│   └── templates/            # HTML frontend
├── tests/                    # Unit tests
├── templates/                # (Optional, if moved here for Flask default)
├── main.py                   # App entry point
├── requirements.txt
└── README.md
```

---

## Features

- ✅ RESTful API using Flask
- ✅ Modular MVC-style code layout
- ✅ Pydantic for input validation
- ✅ SQLite for request logging
- ✅ Simple HTML interface (`/web`)
- ✅ Unit tests for core operations

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourname/math-api.git
cd math-api
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv/Scripts/activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the service

```bash
python main.py
```

### 5. Access the Web Interface and the endpoints

You can access the full interface at:

```
http://127.0.0.1:5000/
```

This will show a landing page with a button to launch the Web UI.

> All operations (Power, Fibonacci, Factorial) are available through the web interface.

---

You can access the endpoints:

| Operation | URL | Method |
|----------|-----|--------|
| Power    | `http://127.0.0.1:5000/math/power` | POST |
| Fibonacci | `http://127.0.0.1:5000/math/fibonacci` | POST |
| Factorial | `http://127.0.0.1:5000/math/factorial` | POST |
| Web UI   | `http://127.0.0.1:5000/web/` | GET |

---

## Sample `curl` Requests

```bash
# Power
curl -X POST http://127.0.0.1:5000/math/power \
  -H "Content-Type: application/json" \
  -d "{\"base\": 2, \"exponent\": 5}"

# Fibonacci
curl -X POST http://127.0.0.1:5000/math/fibonacci \
  -H "Content-Type: application/json" \
  -d "{\"n\": 7}"

# Factorial
curl -X POST http://127.0.0.1:5000/math/factorial \
  -H "Content-Type: application/json" \
  -d "{\"n\": 5}"
```

---

## Testing some unit tests

Run unit tests with:

```bash
python -m unittest discover -s tests
```

---

## Built With

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Flake8](https://flake8.pycqa.org/)

---

## Future Improvements

- Docker support
- JWT Authorization
- Redis-based caching
- Prometheus monitoring
- Kafka-based event logging
- API docs with Swagger/OpenAPI

---

## License

This project is open source under the [MIT License](LICENSE).

---