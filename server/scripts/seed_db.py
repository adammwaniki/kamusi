# scripts/seed_db.py
from app import app, db
from models import SwahiliWord
from services.search_service import SearchService
import random

dummy_data = [
    {
        "word": "jambo",
        "pronunciation": "jah-mboh",
        "translation": "hello",
        "examples": "Jambo rafiki!|Hujambo?",
        "word_class": "greeting"
    },
    {
        "word": "asante",
        "pronunciation": "ah-sahn-teh",
        "translation": "thank you",
        "examples": "Asante sana|Asante kwa msaada",
        "word_class": "expression"
    }
]

def seed_database():
    with app.app_context():
        db.create_all()
        
        for entry in dummy_data:
            if not SwahiliWord.query.filter_by(word=entry['word']).first():
                word = SwahiliWord(**entry)
                db.session.add(word)
        
        db.session.commit()
        print("Database seeded successfully!")
        
        # Index in Elasticsearch
        search_service = SearchService()
        search_service.reindex_all()
        print("Elasticsearch indexed!")

if __name__ == '__main__':
    seed_database()