from flask import Blueprint, jsonify, request
from server.models.movie import Movie
from server.extensions import db
from flask_jwt_extended import jwt_required

movie_bp = Blueprint('movies', __name__, url_prefix='/movies')

@movie_bp.route('', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{
        'id': movie.id,
        'title': movie.title,
        'director': movie.director,
        'year': movie.year,
        'genre': movie.genre,
        'rating': movie.rating
    } for movie in movies])

@movie_bp.route('', methods=['POST'])
@jwt_required()
def add_movie():
    data = request.get_json()
    movie = Movie(
        title=data['title'],
        director=data.get('director'),
        year=data.get('year'),
        genre=data.get('genre'),
        rating=data.get('rating')
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify({'message': 'Movie added successfully'}), 201