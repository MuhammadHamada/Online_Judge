import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def welcome():
    return "Welcome to Online Judge Backend!!"

  # get all users
  @app.route('/users')
  def get_users():

    return None
  
  # create new user
  @app.route('/users', methods=['POST'])
  def create_user():

    return None
  
  # update user's information
  @app.route('/users', methods=['PATCH'])
  def update_user():

    return None

  # get all contests
  @app.route('/contests')
  def get_contests():

    return None
  
  # get users of a contest with contest_id
  @app.route('/contests/<int:contest_id>/users')
  def get_users_of_contest(contest_id):

    return None
  
  # create new contest
  @app.route('/contests', methods=['POST'])
  def create_contest():

    return None

  # update a contest's information
  @app.route('/contests/<int:contest_id>', methods=['PATCH'])
  def update_contest():

    return None
  
  # delete a contest
  @app.route('/contests/<int:contest_id>', methods=['DELETE'])
  def delete_contest(contest_id):

    return None
  

  # get all problems
  @app.route('/problems')
  def get_problems():

    return None

  # get all problems of the contest (with id = contest_id)
  @app.route('/problems/<int:contest_id>')
  def get_problems_of_contest(contest_id):

    return None

  # create new problem
  @app.route('/problems', methods=['POST'])
  def create_problem():

    return None
  
  # delete a problem
  @app.route('/problems/<int:problem_id>', methods=['DELETE'])
  def delete_problem():

    return None

  # get a solution of a problem (with id = problem_id)
  @app.route('/solutions/<int:problem_id>')
  def get_solution():

    return None

  # create a solution of a problem (with id = problem_id)
  @app.route('/solutions/<int:problem_id>', methods=['POST'])
  def create_solution():

    return None

  # get all participations in all contests
  @app.route('/participations')
  def get_participations():

    return None

  # create a new paticipation in a contest
  @app.route('/participate', methods=['POST'])
  def create_participation():

    return None
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)