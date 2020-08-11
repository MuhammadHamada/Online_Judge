import os
from sqlalchemy import Column, String, Integer
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_path = "postgresql://postgres:1234@localhost:5432/online_judge"

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Table():

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        pass

class User(db.Model, Table):
    __tablename__ = 'User'

    id = Column(db.Integer, primary_key=True)
    handle = Column(db.String, nullable=False)
    rating = Column(db.Integer, default=1400, nullable=False)
    level = Column(db.String, default="specialist", nullable=False)
    solutions = db.relationship('Solution', backref='user', lazy=True, cascade="all, delete")
    participations = db.relationship('Participate', backref='user', lazy=True, cascade="all, delete")

    def __init__(self, handle, rating, level):
        self.handle = handle
        self.rating = rating
        self.level = level
    
    def format(self):
        return {
        'id': self.id,
        'handle': self.handle,
        'rating': self.rating,
        'level': self.level}

class Contest(db.Model, Table):
    __tablename__ = 'Contest'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, nullable=False)
    divison = Column(db.Integer, nullable=False)
    time = Column(db.DateTime, nullable=True)
    problems = db.relationship('Problem', backref='contest', lazy=True, cascade="all, delete")
    participations = db.relationship('Participate', backref='contest', lazy=True, cascade="all, delete")

    def __init__(self, name, divison, time):
        self.name = name
        self.divison = divison
        self.time = time
    
    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'divison': self.divison,
        'time': self.time}
    

class Problem(db.Model, Table):
    __tablename__ = 'Problem'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, nullable=False)
    difficulty = Column(db.String, nullable=False)
    text = Column(db.String, nullable=False)
    contest_id = db.Column(db.Integer, db.ForeignKey('Contest.id'), nullable=False)
    solutions = db.relationship('Solution', backref='problem', lazy=True, cascade="all, delete")

    def __init__(self, name, difficulty, text, contest_id):
        self.name = name
        self.difficulty = difficulty
        self.text = text
        self.contest_id = contest_id
    
    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'difficulty': self.difficulty,
        'text': self.text,
        'contest_id': self.contest_id}

class Solution(db.Model, Table):
    __tablename__ = 'Solution'

    id = Column(db.Integer, primary_key=True)
    verdict = Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('Problem.id'), nullable=False)

    def __init__(self, verdict, user_id, problem_id):
        self.verdict = verdict
        self.user_id = user_id
        self.problem_id = problem_id
    
    def format(self):
        return {
        'id': self.id,
        'verdict': self.verdict,
        'user_id': self.user_id,
        'problem_id': self.problem_id}

class Participate(db.Model, Table):
    __tablename__ = "Participate"

    id = Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    contest_id = db.Column(db.Integer, db.ForeignKey('Contest.id'), nullable=False)

    def __init__(self, user_id, contest_id):
        self.user_id = user_id
        self.contest_id = contest_id
    
    def format(self):
        return {
        'id': self.id,
        'user_id': self.user_id,
        'contest_id': self.contest_id}
