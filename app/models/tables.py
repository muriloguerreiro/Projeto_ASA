from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    perfil = db.relationship('Perfil', uselist=False, backref='users')


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username


class Perfil(db.Model):
    __tablename__ = "perfis"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    curso = db.Column(db.String)
    periodo = db.Column(db.Integer)
    disc_1 = db.Column(db.String)
    nota_d1 = db.Column(db.Integer)
    disc_2 = db.Column(db.String)
    nota_d2 = db.Column(db.Integer)
    disc_3 = db.Column(db.String)
    nota_d3 = db.Column(db.Integer)
    disc_4 = db.Column(db.String)
    nota_d4 = db.Column(db.Integer)

    def get_id(self):
        return str(self.id)

    def __init__(self, user_id, curso, periodo, disc_1, disc_2, disc_3, disc_4, nota_d1, nota_d2, nota_d3, nota_d4):
        self.user_id = user_id
        self.curso = curso
        self.periodo = periodo
        self.disc_1 = disc_1
        self.disc_2 = disc_2
        self.disc_3 = disc_3
        self.disc_4 = disc_4
        self.nota_d1 = nota_d1
        self.nota_d2 = nota_d2
        self.nota_d3 = nota_d3
        self.nota_d4 = nota_d4
