from server.extensions import db

class Show(db.Model):
    __tablename__ = 'shows'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    network = db.Column(db.String(50))
    seasons = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    
    def __repr__(self):
        return f'<Show {self.title}>'