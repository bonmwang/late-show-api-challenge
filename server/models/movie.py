from server.extensions import db

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    rating = db.Column(db.Float)
    
    def __repr__(self):
        return f'<Movie {self.title}>'