# Online Judge 

Online judge is a simple website that allow programmers to participate in online programming contests to improve their programming and problem solving skills. It is only backend.

## User Story

### Online Judge has 2 Roles Contestant and Admin

**Contestant's Role**
- Contestant can get all information of users, contests, problems and participations.
- Contestant can participate in contests.
- Contestant can submit to solve problems.
- Contestant can register to the online judge and create new user.

**Admin's Role**
- Admin has all premissions of normal contestants mentioned above.
- Admin can delete contestants(users).
- Admin can delete any contest.
- Admin can delete any problem.
- Admin can create contests.
- Admin can create problems.
- Admin can update users' information.
- Admin can update contests' information.
- Admin can update problems' information.


## Database Design

![Image of database design](https://i.ibb.co/XjZc6bz/ojudge-database.png)

## Topics

- The Final Project of the Full stack Nanodegree
- Database modeling using sqlalchemy (models.py)
- REST API for CRUD using Flask (app.py)
- Authentication & Authorization Role based using Auth0 (auth.py)
- Deployment on Heroku
- Unit testing using unittest (test_app.py)
- Enviroment variables encapsulation (Config.py)

## Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup
```bash
python manage.py db init
python manage.py db migrate
python manage.py db update
```
To insert initial records in the database you must run the server first and open another command window and run the following command.
```bash
python insert_data.py
```

## Run the Server

```bash
python app.py
```

## Run Testing
```bash
python insert_data.py
python test_app.py
.............................
----------------------------------------------------------------------
Ran 29 tests in 74.555s

OK
```

## Enviroment variables
- DATABASE_URL = "postgresql://postgres:1234@localhost:5432/online_judge"
- AUTH0_DOMAIN = 'ojudge.us.auth0.com'
- ALGORITHMS = ['RS256']
- API_AUDIENCE = 'ojudge'
- ADMIN_TOKEN 
- CONTESTANT_TOKEN

**Note:** You must update the envioments variables by updating config.py file. I made this file because i'm working on Windows and running setup.sh didn't work.

## API Reference

### Getting Started

- Base URL: https://ojudge.herokuapp.com/
- Authentication: this version of the application require authentication.

### Error handling
Errors are returned as JSON objects in the following format:
```
{
"success": False, 
"error": 404,
"message": "resource not found"
}
```
The API will return 4 error types when request fail:
```
- 401 Not Authenticated
- 403 Not Authorized
- 404 Resource Not Found
- 422 Not Processable
```

### Endpoints

**Note : All endpoints require Access Token**

#### Admin token
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFQUGQ4eTFyNVdsQ0RGZHB3NkNMSCJ9.eyJpc3MiOiJodHRwczovL29qdWRnZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmIxNWNhMWI0MWYwMDY3ODE3YTBjIiwiYXVkIjoib2p1ZGdlIiwiaWF0IjoxNTk3Nzk4OTgxLCJleHAiOjE1OTc4MDYxODEsImF6cCI6IkFpdzJPOXliVUtyWG9jNGRHWVBpM3BGNThsQW9MeGVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y29udGVzdGFudHMiLCJkZWxldGU6Y29udGVzdHMiLCJkZWxldGU6cHJvYmxlbXMiLCJnZXQ6Y29udGVzdHMiLCJnZXQ6cGFydGljaXBhdGlvbnMiLCJnZXQ6cHJvYmxlbXMiLCJnZXQ6c3VibWlzc2lvbnMiLCJnZXQ6dXNlcnMiLCJwYXRjaDpjb250ZXN0cyIsInBhdGNoOnByb2JsZW1zIiwicGF0Y2g6dXNlcnMiLCJwb3N0OmNvbnRlc3RzIiwicG9zdDpwYXJ0aWNpcGF0aW9ucyIsInBvc3Q6cHJvYmxlbXMiLCJwb3N0OnN1Ym1pc3Npb25zIiwicG9zdDp1c2VycyJdfQ.LKM-zuMkPgVrZupQwMpgg1aqAQVOZzHIpxxtMay5IY4zkz3230x0nuNmu5bw-Mc8H_CyMAGab8e_iUuYAntWpKX33b38c3KcOnN99tOBvlKFmyBcGtQAFHKItfwAX5HLi-sGYg32fZ-fjC1DkvYzLTRoNYighrIUP0jRz6ekHzSAhigVUycMD_uGPQ4K4uY1hBrvMPyFZcTCuSU4-FR1_doa3VHWWBm2QcJ4RmvsejWiGRmtc4ppcLCC5cFOyChAcnHBkW7mjTP6mxqajtnvZCGLzESbUN1NcoPD08xVr3hmvz7vyTEBOtXjEFDlJ2E5G1CzLaU9MSWLYwP1ifh3Eg

#### Contestant token
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFQUGQ4eTFyNVdsQ0RGZHB3NkNMSCJ9.eyJpc3MiOiJodHRwczovL29qdWRnZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmIzMTFhMWI0MWYwMDY3ODE3YTMwIiwiYXVkIjoib2p1ZGdlIiwiaWF0IjoxNTk3Nzk5MDUxLCJleHAiOjE1OTc4MDYyNTEsImF6cCI6IkFpdzJPOXliVUtyWG9jNGRHWVBpM3BGNThsQW9MeGVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y29udGVzdHMiLCJnZXQ6cGFydGljaXBhdGlvbnMiLCJnZXQ6cHJvYmxlbXMiLCJnZXQ6c3VibWlzc2lvbnMiLCJnZXQ6dXNlcnMiLCJwb3N0OnBhcnRpY2lwYXRpb25zIiwicG9zdDpzdWJtaXNzaW9ucyIsInBvc3Q6dXNlcnMiXX0.c_V2HhJ3heyX_KPNprDuIapkLrqnnhyROQwzwk9flhTKeQUnShyUKCvpLhKvLznYyTcnDTVGSUlpujFnFT5HZpqH-pYiF36zKNyQS2m5jUmTRXJc86pJHQ1MBKpJYB3ZhKxHGQdGXj7Ix97kllgb7B2v_K0YUSjX6iOZ6Gv1-iKLuhQJLA_GKKOL9PfPlaomcaqIlCfIdcQxr8pKksoEI181qUm0TL5i5_ZmSBtqdrb1FsoNVd-1sI0AFBVo9Sby7RCEmY3c_Hztpd_6WsIYqqHFfW-V4ctmrGSg_mtyjVmtCQLdMuDkJU-8FqR1dmAj0sJapJ63ttmFuCacfIhnfg

**All endpoints is tested on Postman**

#### GET /users

#### POST /users

#### PATCH /users/<int:user_id>

#### DELETE /users/<int:user_id>

#### GET /contests

#### GET /contests/<int:contest_id>/users

#### POST /contests

#### PATCH /contests/<int:contest_id>

#### DELETE /contests/<int:contest_id>

#### GET /problems

#### GET /contests/<int:contest_id>/problems

#### POST /problems

#### DELETE /problems/<int:problem_id>

#### GET /submissions

#### GET /submissions/<int:problem_id>

#### POST /submissions

#### GET /participations

#### POST /participate
