from flask import Blueprint, jsonify, abort, request
from sqlalchemy.orm import relationship
from ..models import Anime, Genre, Studio, db
from flask import Blueprint

bp = Blueprint('anime', __name__, url_prefix='/anime')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    anime = Anime.query.all()  # ORM performs SELECT query
    result = []
    for a in anime:
        result.append(a.serialize())  # build list of Anime as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Anime.query.get_or_404(id)
    return jsonify(a.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'anime_title' not in request.json or 'studio_id' not in request.json:
        return abort(400)
    Studio.query.get_or_404(request.json['studio_id'])
    a = Anime(
        anime_title=request.json['anime_title'],
        studio_id=request.json['studio_id']
    )
    db.session.add(a)
    db.session.commit()
    return jsonify(a.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a = Anime.query.get_or_404(id)
    try:
        db.session.delete(a)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:id>/genres', methods=['GET'])
def get_genres(id: int):
    a = Anime.query.get_or_404(id)
    result = []
    for genre in a.genre_list:
        result.append(genre.serialize())
    return jsonify(result)
