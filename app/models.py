from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

#New login changes.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Feedback(db.Model):
    
    __tablename__ = 'feedback'

    id = db.Column(db.Integer,primary_key=True)
    company = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('Likes',backref='post',lazy='dynamic')
    dislikes = db.relationship('Dislikes',backref='post',lazy='dynamic')
    comment = db.relationship('Comment',backref='post',lazy='dynamic')

    def save_feedback(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Feedback{self.company}'
class User(UserMixin, db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True)
    bio = db.Column(db.String(255))
    avatar = db.Column(db.String())
    email = db.Column(db.String(255),unique= True,index = True)
    password_hash = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    feedback_id = db.Column(db.Integer,db.ForeignKey('feedback.id'))
    feedback_comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, feedback_id):
        comments = Comment.query.filter_by(feedback_id = feedback_id).all()
        return comments

    @classmethod
    def get_comment_writer(cls, user_id):
        writer = User.query.filter_by(id=user_id).first()

        return writer

class Dislikes(db.Model):
    _tablename_ = 'dislikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        dislikes = Dislikes.query.filter_by(feedback_id = id).all()
        return dislikes

    def _repr_(self):
        return f'{self.user_id}:{self.feedback_id}'

class Likes(db.Model):
    _tablename_ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    feedback_id = db.Column(db.Integer, db.ForeignKey('feedback.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        likes = Likes.query.filter_by(feedback_id=id).all()
        return likes

    def _repr_(self):
        return f'{self.user_id}:{self.feedback_id}'

class Role(db.Model):
    
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'