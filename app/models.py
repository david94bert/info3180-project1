from . import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    biography = db.Column(db.Text)
    photo_name = db.Column(db.LargeBinary)
    date_created = db.Column(db.DateTime)
    
    def __init__(self, id, firstname, lastname, gender, email, location, biography, photo_name, date_created):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.biography=biography
        self.photo_name=photo_name
        self.date_created=date_created
    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)