import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import create_app
from server.models import db, User, Movie, Show
from datetime import datetime

app = create_app()

def seed_data():
    with app.app_context():
        
        db.drop_all()
        db.create_all()

        
        admin = User(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        
        movies = [
            Movie(title="The Shawshank Redemption", director="Frank Darabont", year=1994, genre="Drama", rating=9.3),
            Movie(title="The Godfather", director="Francis Ford Coppola", year=1972, genre="Crime", rating=9.2),
            Movie(title="Pulp Fiction", director="Quentin Tarantino", year=1994, genre="Crime", rating=8.9),
            Movie(title="The Dark Knight", director="Christopher Nolan", year=2008, genre="Action", rating=9.0)
        ]
        db.session.add_all(movies)

        
        shows = [
            Show(title="Breaking Bad", network="AMC", seasons=5, episodes=62, genre="Crime"),
            Show(title="Game of Thrones", network="HBO", seasons=8, episodes=73, genre="Fantasy"),
            Show(title="Stranger Things", network="Netflix", seasons=4, episodes=34, genre="Sci-Fi")
        ]
        db.session.add_all(shows)

        db.session.commit()
        print("Database seeded with 4 movies and 3 TV shows!")

if __name__ == '__main__':
    seed_data()