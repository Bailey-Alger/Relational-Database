from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

anime_genres_table = db.Table(
    'anime_genres',
    db.Column(
        'anime_id', db.Integer,
        db.ForeignKey('anime.id'),
        primary_key=True
    ),

    db.Column(
        'genre_id', db.Integer,
        db.ForeignKey('genres.id'),
        primary_key=True
    )
)


class Anime(db.Model):
    __tablename__ = 'anime'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    anime_title = db.Column(db.String(128), unique=True, nullable=False)
    media_type = db.Column(db.String(128))
    studio_id = db.Column(
        db.Integer, db.ForeignKey('studios.id'), nullable=False)
    genre_list = db.relationship(
        'Genre', secondary=anime_genres_table,
        lazy='subquery',
        backref=db.backref('genre_backref', lazy=True)
    )

    def __init__(self, anime_title: str, studio_id: int):
        self.anime_title = anime_title
        self.studio_id = studio_id

    def serialize(self):
        return {
            'id': self.id,
            'anime_title': self.anime_title,
            'studio_id': self.studio_id
        }


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Main_Character(db.Model):
    __tablename__ = 'main_characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_name = db.Column(db.String(128), nullable=False)
    anime_id = db.Column(
        db.Integer, db.ForeignKey('anime.id'), nullable=False)

    def __init__(self, character_name: str, anime_id: int):
        self.character_name = character_name
        self.anime_id = anime_id

    def serialize(self):
        return {
            'id': self.id,
            'character_name': self.character_name,
            'anime_id': self.anime_id
        }


class Studio(db.Model):
    __tablename__ = 'studios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    studio_name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, studio_name: str):
        self.studio_name = studio_name

    def serialize(self):
        return {
            'id': self.id,
            'studio_name': self.studio_name
        }
