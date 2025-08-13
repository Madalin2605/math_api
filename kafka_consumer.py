from kafka import KafkaConsumer
import json

# Kafka configuration
TOPIC = "math-api-logs"
BROKER = "localhost:9092"  # Replace with your Kafka NodePort or cloud broker

# Create consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[BROKER],
    auto_offset_reset='earliest',       # Read all logs from the beginning
    enable_auto_commit=True,
    group_id='math-api-consumer',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print(f"✅ Listening for messages on topic '{TOPIC}' ...\n")

# Listen and display logs
for message in consumer:
    print("🔔 New message received:")
    print(json.dumps(message.value, indent=2))
    print("-" * 40)
