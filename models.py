import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserRecord(db.Model):
    __tablename__ = 'user_records'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<UserRecord {self.name}>'