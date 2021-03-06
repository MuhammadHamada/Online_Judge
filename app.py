#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, User, Contest, Problem, Submission, \
    Participate
from auth import AuthError, requires_auth


def create_app(test_config=None):

    # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE')
        return response

    @app.route('/')
    def welcome():
        return 'Welcome to Online Judge Backend!!'

    # get all users

    @app.route('/users', methods=['GET'])
    @requires_auth('get:users')
    def get_users():

        users = User.query.order_by(User.id).all()
        current_users = [user.format() for user in users]

        return jsonify({'success': True, 'users': current_users,
                        'total_users': len(current_users)})

    # create new user

    @app.route('/users', methods=['POST'])
    @requires_auth('post:users')
    def create_user():

        try:
            handle = request.get_json()['handle']
            rating = request.get_json()['rating']
            level = request.get_json()['level']

            user = User(handle=handle, rating=rating, level=level)
            user.insert()

            return jsonify({'success': True, 'user_id': user.id})
        except BaseException:

            abort(422)

    # update user's information

    @app.route('/users/<int:user_id>', methods=['PATCH'])
    @requires_auth('patch:users')
    def update_user(user_id):

        flag = False
        try:
            user = User.query.filter(User.id == user_id).one_or_none()
            if user is None:
                flag = True
                abort(404)

            if 'handle' in request.get_json():
                user.handle = request.get_json()['handle']
            if 'rating' in request.get_json():
                user.rating = request.get_json()['rating']
            if 'level' in request.get_json():
                user.level = request.get_json()['level']

            user.update()

            return jsonify({'success': True, 'user': user.format()})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # delete a user

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    @requires_auth('delete:contestants')
    def delete_user(user_id):

        flag = False
        try:
            user = User.query.filter(User.id == user_id).one_or_none()
            if user is None:
                flag = True
                abort(404)

            user.delete()
            return jsonify({'success': True, 'deleted': user_id})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # get all contests

    @app.route('/contests', methods=['GET'])
    @requires_auth('get:contests')
    def get_contests():

        contests = Contest.query.order_by(Contest.id).all()
        all_contests = [contest.format() for contest in contests]

        return jsonify({'success': True, 'contests': all_contests,
                        'total_contests': len(all_contests)})

    # get handles of users in a contest with contest_id

    @app.route('/contests/<int:contest_id>/users', methods=['GET'])
    @requires_auth('get:contests')
    def get_users_of_contest(contest_id):

        flag = False
        try:

            selection = Participate.query.filter(
                Participate.contest_id == contest_id).all()
            if len(selection) == 0:
                flag = True
                abort(404)

            users = User.query.join(Participate).filter(
                Participate.contest_id == contest_id).filter(
                Participate.user_id == User.id).all()
            handles = [user.handle for user in users]

            return jsonify({'success': True, 'handles': handles})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # create new contest

    @app.route('/contests', methods=['POST'])
    @requires_auth('post:contests')
    def create_contest():

        try:
            name = request.get_json()['name']
            divison = request.get_json()['divison']
            time = request.get_json()['time']

            contest = Contest(name=name, divison=divison, time=time)
            contest.insert()

            return jsonify({'success': True, 'contest_id': contest.id})
        except BaseException:

            abort(422)

    # update a contest's information

    @app.route('/contests/<int:contest_id>', methods=['PATCH'])
    @requires_auth('patch:contests')
    def update_contest(contest_id):

        flag = False
        try:
            contest = Contest.query.filter(Contest.id
                                           == contest_id).one_or_none()
            if contest is None:
                flag = True
                abort(404)

            if 'name' in request.get_json():
                contest.name = request.get_json()['name']
            if 'divison' in request.get_json():
                contest.divison = request.get_json()['divison']
            if 'time' in request.get_json():
                contest.time = request.get_json()['time']

            contest.update()

            return jsonify({'success': True,
                            'contest': contest.format()})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # delete a contest

    @app.route('/contests/<int:contest_id>', methods=['DELETE'])
    @requires_auth('delete:contests')
    def delete_contest(contest_id):

        flag = False
        try:
            contest = Contest.query.get(contest_id)
            if contest is None:
                flag = True
                abort(404)

            contest.delete()

            return jsonify({'success': True, 'deleted': contest_id})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # get all problems

    @app.route('/problems', methods=['GET'])
    @requires_auth('get:problems')
    def get_problems():

        problems = Problem.query.order_by(Problem.id).all()
        all_problems = [problem.format() for problem in problems]

        return jsonify({'success': True, 'problems': all_problems,
                        'total_problems': len(all_problems)})

    # get all problems of the contest (with id = contest_id)

    @app.route('/contests/<int:contest_id>/problems', methods=['GET'])
    @requires_auth('get:problems')
    def get_problems_of_contest(contest_id):

        problems = Problem.query.filter(
            Problem.contest_id == contest_id).order_by(
            Problem.id).all()
        all_contest_problems = [problem.format() for problem in
                                problems]

        return jsonify({
            'success': True,
            'contest_id': contest_id,
            'problems': all_contest_problems,
            'total_problems': len(all_contest_problems),
        })

    # create new problem

    @app.route('/problems', methods=['POST'])
    @requires_auth('post:problems')
    def create_problem():

        try:
            name = request.get_json()['name']
            difficulty = request.get_json()['difficulty']
            text = request.get_json()['text']
            contest_id = request.get_json()['contest_id']

            problem = Problem(name=name, difficulty=difficulty,
                              text=text, contest_id=contest_id)
            problem.insert()

            return jsonify({'success': True, 'problem_id': problem.id})
        except BaseException:

            abort(422)

    # delete a problem

    @app.route('/problems/<int:problem_id>', methods=['DELETE'])
    @requires_auth('delete:problems')
    def delete_problem(problem_id):

        flag = False
        try:
            problem = Problem.query.filter(Problem.id
                                           == problem_id).one_or_none()
            if problem is None:
                flag = True
                abort(404)

            problem.delete()

            return jsonify({'success': True, 'deleted': problem_id})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # get all submissions on the online judge

    @app.route('/submissions', methods=['GET'])
    @requires_auth('get:submissions')
    def get_all_submissions():

        submissions = Submission.query.order_by(Submission.id).all()
        all_submissions = [submission.format() for submission in
                           submissions]

        return jsonify({'success': True,
                        'submissions': all_submissions,
                        'total_submissions': len(all_submissions)})

    # get a submission of a problem (with id = problem_id)

    @app.route('/submissions/<int:problem_id>', methods=['GET'])
    @requires_auth('get:submissions')
    def get_problem_submissions(problem_id):

        submissions = Submission.query.filter(
            Submission.problem_id == problem_id).order_by(
            Submission.id).all()
        all_problem_submission = [submission.format() for submission in
                                  submissions]

        return jsonify({
            'success': True,
            'problem_id': problem_id,
            'submissions': all_problem_submission,
            'total_submissions': len(all_problem_submission),
        })

    # create a submission of a problem (with id = problem_id)

    @app.route('/submissions', methods=['POST'])
    @requires_auth('post:submissions')
    def create_submission():

        flag = False
        try:
            code = request.get_json()['code']
            verdict = request.get_json()['verdict']
            user_id = request.get_json()['user_id']
            problem_id = request.get_json()['problem_id']

            user = User.query.filter(User.id == user_id).one_or_none()
            problem = Problem.query.filter(Problem.id
                                           == problem_id).one_or_none()

            if user is None or problem is None:
                flag = True
                abort(404)

            submission = Submission(code=code, verdict=verdict,
                                    user_id=user_id,
                                    problem_id=problem_id)
            submission.insert()

            return jsonify({'success': True,
                            'submission_id': submission.id})
        except BaseException:

            if flag:
                abort(404)
            else:
                abort(422)

    # get all participations in all contests

    @app.route('/participations', methods=['GET'])
    @requires_auth('get:participations')
    def get_participations():

        participations = \
            Participate.query.order_by(Participate.id).all()
        all_participations = [participation.format()
                              for participation in participations]

        return jsonify({'success': True,
                        'participations': all_participations,
                        'total_participations': len(all_participations)})

    # create a new paticipation in a contest

    @app.route('/participate', methods=['POST'])
    @requires_auth('post:participations')
    def create_participation():

        flag = False
        try:

            user_id = request.get_json()['user_id']
            contest_id = request.get_json()['contest_id']

            user = User.query.filter(User.id == user_id).one_or_none()
            contest = Contest.query.filter(Contest.id
                                           == contest_id).one_or_none()

            if user is None or contest is None:
                flag = True
                abort(404)

            paticipation = Participate(user_id=user_id,
                                       contest_id=contest_id)
            paticipation.insert()

            return jsonify({'success': True,
                            'paticipation_id': paticipation.id})
        except BaseException:
            if flag:
                abort(404)
            else:
                abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False, 'error': 404,
                         'message': 'resource not found'}), 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                         'message': 'unprocessable'}), 422)

    @app.errorhandler(AuthError)
    def auth_error(e):
        return (jsonify(e.error), e.status_code)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
