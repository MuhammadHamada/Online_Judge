import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, User, Contest, Problem, Submission, Participate

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def welcome():
    return "Welcome to Online Judge Backend!!"

  # get all users
  @app.route('/users', methods=['GET'])
  def get_users():

    users = User.query.order_by(User.id).all()
    current_users = [user.format() for user in users]

    return jsonify ({
      'success': True,
      'users' : current_users,
      'total_users' : len(current_users)
    })
  
  # create new user
  @app.route('/users', methods=['POST'])
  def create_user():

    return None
  
  # update user's information
  @app.route('/users', methods=['PATCH'])
  def update_user():

    return None

  # get all contests
  @app.route('/contests', methods=['GET'])
  def get_contests():

    contests = Contest.query.order_by(Contest.id).all()
    all_contests = [contest.format() for contest in contests]

    return jsonify ({
      'success': True,
      'contests' : all_contests,
      'total_contests' : len(all_contests)
    })
  
  # get handles of users in a contest with contest_id
  @app.route('/contests/<int:contest_id>/users', methods=['GET'])
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
    
    try:
        contest = Contest.query.filter(Contest.id == contest_id).one_or_none()
        if contest is None:
            abort(404)

        contest.delete()

        return jsonify({
            "success": True,
            "deleted": contest_id
        })

    except BaseException:
            abort(422)
  

  # get all problems
  @app.route('/problems', methods=['GET'])
  def get_problems():

    problems = Problem.query.order_by(Problem.id).all()
    all_problems = [problem.format() for problem in problems]

    return jsonify ({
      'success': True,
      'problems' : all_problems,
      'total_problems' : len(all_problems)
    })

  # get all problems of the contest (with id = contest_id)
  @app.route('/problems/<int:contest_id>', methods=['GET'])
  def get_problems_of_contest(contest_id):

    problems = Problem.query.filter(Problem.contest_id == contest_id).order_by(Problem.id).all()
    all_contest_problems = [problem.format() for problem in problems]

    return jsonify ({
      'success': True,
      'contest_id' : contest_id,
      'problems' : all_contest_problems,
      'total_problems' : len(all_contest_problems)
    })

  # create new problem
  @app.route('/problems', methods=['POST'])
  def create_problem():

    return None
  
  # delete a problem
  @app.route('/problems/<int:problem_id>', methods=['DELETE'])
  def delete_problem(problem_id):

    try:
        problem = Problem.query.filter(Problem.id == problem_id).one_or_none()
        if problem is None:
            abort(404)

        problem.delete()

        return jsonify({
            "success": True,
            "deleted": problem_id
        })

    except BaseException:
            abort(422)

  # get a submission of a problem (with id = problem_id)
  @app.route('/submissions/<int:problem_id>', methods=['GET'])
  def get_submission(problem_id):

    submissions = Submission.query.filter(Submission.problem_id == problem_id).order_by(Submission.id).all()
    all_problem_submission = [submission.format() for submission in submissions]

    return jsonify ({
      'success': True,
      'problem_id' : problem_id,
      'submissions' : all_problem_submission,
      'total_submissions' : len(all_problem_submission)
    })

  # create a submission of a problem (with id = problem_id)
  @app.route('/submissions/<int:problem_id>', methods=['POST'])
  def create_submission(problem_id):

    return None

  # get all participations in all contests
  @app.route('/participations', methods=['GET'])
  def get_participations():

    participations = Participate.query.order_by(Participate.id).all()
    all_participations = [participation.format() for participation in participations]

    return jsonify ({
      'success': True,
      'participations' : all_participations,
      'total_participations' : len(all_participations)
    })

  # create a new paticipation in a contest
  @app.route('/participate', methods=['POST'])
  def create_participation():

    return None
  
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)