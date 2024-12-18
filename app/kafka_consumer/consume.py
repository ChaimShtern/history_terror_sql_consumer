import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from app.db.database import session_maker
from app.repository.xhfdgf import parse_and_save

load_dotenv(verbose=True)


def consume(mode='latest'):
    consumer = KafkaConsumer(
        os.environ["STATISTICS_TOPIC"],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset=mode
    )
    for message in consumer:
        parse_and_save(message.value, session_maker)
