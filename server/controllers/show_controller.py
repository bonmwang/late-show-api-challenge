from flask import Blueprint, jsonify, request
from server.models.show import Show
from server.extensions import db
from flask_jwt_extended import jwt_required

show_bp = Blueprint('shows', __name__, url_prefix='/shows')

@show_bp.route('', methods=['GET'])
def get_shows():
    shows = Show.query.all()
    return jsonify([{
        'id': show.id,
        'title': show.title,
        'network': show.network,
        'seasons': show.seasons,
        'episodes': show.episodes,
        'genre': show.genre
    } for show in shows])

@show_bp.route('', methods=['POST'])
@jwt_required()
def add_show():
    data = request.get_json()
    show = Show(
        title=data['title'],
        network=data.get('network'),
        seasons=data.get('seasons'),
        episodes=data.get('episodes'),
        genre=data.get('genre')
    )
    db.session.add(show)
    db.session.commit()
    return jsonify({'message': 'TV show added successfully'}), 201