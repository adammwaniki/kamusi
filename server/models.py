from app import db

class SwahiliWord(db.Model):
    __tablename__ = 'swahili_words'
    
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255), unique=True, nullable=False)
    pronunciation = db.Column(db.String(255))
    translation = db.Column(db.Text, nullable=False)
    examples = db.Column(db.Text)
    word_class = db.Column(db.String(50))
    synonyms = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'pronunciation': self.pronunciation,
            'translation': self.translation,
            'examples': self.examples.split('|') if self.examples else [],
            'word_class': self.word_class,
            'synonyms': self.synonyms.split(',') if self.synonyms else []
        }