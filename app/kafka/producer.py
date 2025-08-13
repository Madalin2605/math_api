import json
import logging
from datetime import datetime
from kafka import KafkaProducer

# Configuration (adjust port as needed)
KAFKA_TOPIC = "math-api-logs"
KAFKA_BROKER = "localhost:9092"  # Use NodePort or cloud host if needed

# Initialize Kafka producer
try:
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    logging.info("[Kafka] Producer initialized")
except Exception as e:
    producer = None
    logging.error(f"[Kafka] Failed to initialize producer: {e}")

# Function to send structured log
def send_log(operation: str, input_data: dict, result: str):
    if not producer:
        logging.warning("[Kafka] Kafka producer not available — skipping send_log")
        return

    payload = {
        "operation": operation,
        "input": input_data,
        "result": result,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        producer.send(KAFKA_TOPIC, value=payload)
        producer.flush()
        logging.info(f"[Kafka] Log sent to topic {KAFKA_TOPIC}")
    except Exception as e:
        logging.error(f"[Kafka] Failed to send message: {e}")
