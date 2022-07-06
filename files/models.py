from files import db

class Artist(db.Model):
    __tablename__  = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date_of_birth = db.Column(db.date, nullable=False)
    bio = db.Column(db.String(256), nullable=False)
    songs = db.relationship('ArtistSong', backref='artist')
    
    def __repr__(self):
        return f"User id is: {self.id} and name is: {self.name}"


class User(db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)



class Song(db.Model):
    __tablename__  = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date_of_release = db.Column(db.date, nullable=False)
    cover_image = db.column(db.String(256), nullable=False)
    artists = db.relationship('ArtistSong', backref='song')

    def __repr__(self):
        return f"Song id is: {self.id} and name is: {self.name}"



class ArtistSong(db.Model):
    __tablename__  = 'artist-song'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    song = db.Column(db.Integer, db.ForeginKey('Song.id'))
    artist = db.Column(db.Integer, db.ForeginKey('artist.id'))

