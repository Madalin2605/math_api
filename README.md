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
│   ├── kafka/                # Kafka producer integration
│   └── templates/            # HTML frontend (Bootstrap-based)
├── tests/                    # Unit tests
├── kafka_consumer.py         # Standalone Kafka consumer for logs
├── docker-compose.yml        # Kafka + Zookeeper setup for local use
├── main.py                   # Flask app entry point
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

## How to Run the Project (With Optional Kafka Logging)

This section describes the complete flow to set up and run the Math API microservice, including optional Kafka-based log streaming.

### 1. Clone the repository

```bash
git clone https://github.com/yourname/math-api.git
cd math-api
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv/Scripts/activate on Windows (bash)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. (Optional) Enable Kafka Logging for API Requests

If you want to stream logs from your Flask app to Kafka in real-time, follow these extra steps.

#### a. Start Kafka and Zookeeper using Docker Compose

```bash
docker compose up -d
```

Or with Rancher Desktop:

```bash
nerdctl compose up -d
```

Kafka will be available at `localhost:9092`.

#### b. Start the Kafka Consumer (in a new terminal)

```bash
python kafka_consumer.py
```

This will listen to the `math-api-logs` topic and display messages as they arrive.

---

### 5. Run the service (the Flask Application)

```bash
python main.py
```

### 6. Access the Web Interface and the endpoints

You can access the full interface at:

```
http://127.0.0.1:5000/
```

This will show a landing page with a button to launch the Web UI.

> All operations (Power, Fibonacci, Factorial) are available through the web interface — the results will display in the UI and logs will stream to Kafka (if enabled).

---

### 7. API Endpoints

These endpoints can also be triggered directly using tools like `curl` or Postman:

| Operation | URL | Method |
|----------|-----|--------|
| Power    | `http://127.0.0.1:5000/math/power` | POST |
| Fibonacci | `http://127.0.0.1:5000/math/fibonacci` | POST |
| Factorial | `http://127.0.0.1:5000/math/factorial` | POST |
| Web UI   | `http://127.0.0.1:5000/web/` | GET |

---

### 8. Shut Down Services

To stop Kafka and Zookeeper:

```bash
docker compose down
```

To clear all Kafka data:

```bash
docker compose down -v
```

To stop the Flask app and Kafka consumer, just Ctrl+C in each terminal.

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

## License

This project is open source under the [MIT License](LICENSE).

---