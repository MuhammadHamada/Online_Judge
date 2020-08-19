import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from app import create_app
from models import setup_db, User, Contest, Problem, Submission, Participate, database_path, db

from config import ADMIN_TOKEN, CONTESTANT_TOKEN


class OnlineJudgeTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, database_path)
        self.admin = {"Authorization": "Bearer " + ADMIN_TOKEN}
        self.contestant = {"Authorization": "Bearer " + CONTESTANT_TOKEN}

    def tearDown(self):
        """Executed after reach test"""
        pass

    # ---------- Users Testing ------------------------
    def test_get_users(self):
        res = self.client().get('/users', headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['users'])
        self.assertTrue(data['total_users'])

    def test_non_authenticated_cannot_get_users(self):
        res = self.client().get('/users')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_create_user(self):
        new_user = {
            "handle": "new_user1",
            "level": "specialist",
            "rating": 1400
        }
        res = self.client().post('/users', json=new_user, headers=self.admin)
        data = json.loads(res.data)

        self.client().delete('/users/' +
                             str(data['user_id']), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['user_id'])

    def test_admin_can_delete_user(self):
        new_user = {
            "handle": "new_user2",
            "level": "specialist",
            "rating": 1400
        }
        res = self.client().post('/users', json=new_user, headers=self.contestant)
        data = json.loads(res.data)

        res = self.client().delete('/users/' +
                                   str(data['user_id']), headers=self.admin)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_admin_cannot_delete_not_exist_user(self):

        res = self.client().delete('/users/100000', headers=self.admin)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_contestant_cannot_delete_user(self):
        new_user = {
            "handle": "new_user3",
            "level": "specialist",
            "rating": 1400
        }
        res = self.client().post('/users', json=new_user, headers=self.contestant)
        data = json.loads(res.data)
        user_id = data['user_id']

        res = self.client().delete('/users/' + str(user_id), headers=self.contestant)
        data = json.loads(res.data)

        self.client().delete('/users/' + str(user_id), headers=self.admin)

        self.assertEqual(res.status_code, 403)

    def test_admin_can_update_user(self):
        new_user = {
            "handle": "new_user4",
            "level": "specialist",
            "rating": 1400
        }
        res = self.client().post('/users', json=new_user, headers=self.contestant)
        data = json.loads(res.data)
        user_id = data['user_id']

        new_user = {
            "handle": "NEW_user4",
            "level": "expert",
            "rating": 1600
        }

        res = self.client().patch(
            '/users/' + str(user_id),
            json=new_user,
            headers=self.admin)
        data = json.loads(res.data)

        self.client().delete('/users/' + str(user_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['user']['handle'], "NEW_user4")
        self.assertEqual(data['user']['level'], "expert")
        self.assertEqual(data['user']['rating'], 1600)

    def test_admin_cannot_update_not_exist_user(self):

        user = {
            "handle": "user",
            "level": "expert",
            "rating": 1600
        }

        res = self.client().patch('/users/100000', json=user, headers=self.admin)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_contestant_cannot_update_user(self):
        new_user = {
            "handle": "new_user4",
            "level": "specialist",
            "rating": 1400
        }
        res = self.client().post('/users', json=new_user, headers=self.contestant)
        data = json.loads(res.data)
        user_id = data['user_id']

        new_user = {
            "handle": "NEW_user4",
            "level": "expert",
            "rating": 1600
        }

        res = self.client().patch(
            '/users/' + str(user_id),
            json=new_user,
            headers=self.contestant)
        data = json.loads(res.data)

        self.client().delete('/users/' + str(user_id), headers=self.admin)

        self.assertEqual(res.status_code, 403)

    # ---------- Contests Testing ------------------------

    def test_get_contests(self):
        res = self.client().get('/contests', headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['contests'])
        self.assertTrue(data['total_contests'])

    def test_get_users_of_contest(self):

        min_id = db.session.query(func.min(Contest.id)).scalar()
        res = self.client().get(
            '/contests/' + str(min_id) + '/users',
            headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['handles'])

    def test_admin_can_create_contest(self):

        new_contest = {
            "name": "new_contest1",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['contest_id'])

    def test_contestant_cannot_create_contest(self):

        new_contest = {
            "name": "new_contest2",
            "divison": 1
        }

        res = self.client().post('/contests', json=new_contest, headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    def test_admin_can_update_contest(self):

        new_contest = {
            "name": "new_contest3",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_contest = {
            "name": "NEW_Contest_3",
        }

        res = self.client().patch(
            '/contests/' + str(contest_id),
            json=new_contest,
            headers=self.admin)
        data = json.loads(res.data)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['contest']["name"], "NEW_Contest_3")

    def test_contestant_cannot_update_contest(self):

        new_contest = {
            "name": "new_contest4",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_contest = {
            "name": "NEW_Contest4"
        }

        res = self.client().patch(
            '/contests/' + str(contest_id),
            json=new_contest,
            headers=self.contestant)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 403)

    def test_admin_can_delete_contest(self):

        new_contest = {
            "name": "new_contest5",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        res = self.client().delete('/contests/' + str(contest_id), headers=self.admin)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], contest_id)

    def test_admin_cannot_delete_not_exist_contest(self):

        max_id = db.session.query(func.max(Contest.id)).scalar() + 10
        res = self.client().delete('/contests/' + str(max_id), headers=self.admin)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_contestant_cannot_delete_contest(self):

        new_contest = {
            "name": "new_contest5",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        res = self.client().delete(
            '/contests/' + str(contest_id),
            headers=self.contestant)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 403)

    def test_get_contest_problems(self):

        min_id = db.session.query(func.min(Contest.id)).scalar()
        res = self.client().get(
            '/contests/' + str(min_id) + '/problems',
            headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['contest_id'], min_id)
        self.assertTrue(data['problems'])
        self.assertTrue(data['total_problems'])

    # ---------- Problems Testing ------------------------

    def test_get_problems(self):
        res = self.client().get('/problems', headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['problems'])
        self.assertTrue(data['total_problems'])

    def test_admin_can_create_problem(self):

        new_contest = {
            "name": "new_contest5",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_problem = {
            "name": "new_problem1",
            "difficulty": "A",
            "text": "problem text",
            "contest_id": contest_id
        }

        res = self.client().post('/problems', json=new_problem, headers=self.admin)
        data = json.loads(res.data)
        problem_id = data['problem_id']

        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['problem_id'])

    def test_admin_can_delete_problem(self):

        new_contest = {
            "name": "new_contest6",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_problem = {
            "name": "new_problem2",
            "difficulty": "A",
            "text": "problem text",
            "contest_id": contest_id
        }

        res = self.client().post('/problems', json=new_problem, headers=self.admin)
        data = json.loads(res.data)
        problem_id = data['problem_id']

        res = self.client().delete('/problems/' + str(problem_id), headers=self.admin)
        data = json.loads(res.data)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_admin_cannot_delete_not_exist_problem(self):

        max_id = db.session.query(func.max(Problem.id)).scalar() + 10
        res = self.client().delete('/problems/' + str(max_id), headers=self.admin)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    def test_contestant_cannot_delete_problem(self):

        new_contest = {
            "name": "new_contest6",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_problem = {
            "name": "new_problem3",
            "difficulty": "A",
            "text": "problem text",
            "contest_id": contest_id
        }

        res = self.client().post('/problems', json=new_problem, headers=self.admin)
        data = json.loads(res.data)
        problem_id = data['problem_id']

        res = self.client().delete(
            '/problems/' + str(problem_id),
            headers=self.contestant)
        data = json.loads(res.data)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 403)

    # ---------- Submissions Testing ------------------------
    def test_get_all_submissions(self):
        res = self.client().get('/submissions', headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['submissions'])
        self.assertTrue(data['total_submissions'])

    def test_get_problem_submissions(self):

        min_id = db.session.query(func.min(Problem.id)).scalar()
        res = self.client().get('/submissions/' + str(min_id), headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['problem_id'], min_id)
        self.assertTrue(data['submissions'])
        self.assertTrue(data['total_submissions'])

    def test_create_submission(self):

        new_user = {
            "handle": "new_user7",
            "level": "expert",
            "rating": 1660
        }

        res = self.client().post('/users', json=new_user, headers=self.admin)
        data = json.loads(res.data)
        user_id = data['user_id']

        new_contest = {
            "name": "new_contest7",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_problem = {
            "name": "new_problem4",
            "difficulty": "A",
            "text": "problem text",
            "contest_id": contest_id
        }

        res = self.client().post('/problems', json=new_problem, headers=self.admin)
        data = json.loads(res.data)
        problem_id = data['problem_id']

        new_submission = {
            "code": "code of the submission",
            "verdict": "Accepted",
            "user_id": user_id,
            "problem_id": problem_id
        }

        res = self.client().post(
            '/submissions',
            json=new_submission,
            headers=self.contestant)
        data = json.loads(res.data)

        self.client().delete('/users/' + str(user_id), headers=self.admin)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['submission_id'])

    def test_get_participations(self):

        res = self.client().get('/participations', headers=self.contestant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['participations'])
        self.assertTrue(data['total_participations'])

    def test_create_participation(self):

        new_user = {
            "handle": "new_user8",
            "level": "expert",
            "rating": 1660
        }

        res = self.client().post('/users', json=new_user, headers=self.admin)
        data = json.loads(res.data)
        user_id = data['user_id']

        new_contest = {
            "name": "new_contest8",
            "divison": 1,
            "time": None
        }

        res = self.client().post('/contests', json=new_contest, headers=self.admin)
        data = json.loads(res.data)
        contest_id = data['contest_id']

        new_paticipation = {
            "user_id": user_id,
            "contest_id": contest_id
        }

        res = self.client().post(
            '/participate',
            json=new_paticipation,
            headers=self.contestant)
        data = json.loads(res.data)

        self.client().delete('/users/' + str(user_id), headers=self.admin)
        self.client().delete('/contests/' + str(contest_id), headers=self.admin)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['paticipation_id'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
