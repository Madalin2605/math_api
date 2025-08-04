from datetime import datetime
from app.models.db import db


class RequestLog(db.Model):
    __tablename__ = 'request_logs'

    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(50), nullable=False)
    input_data = db.Column(db.String(200), nullable=False)
    result = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
