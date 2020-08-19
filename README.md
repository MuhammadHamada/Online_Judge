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


## Getting Started

- URL: [https://ojudge.herokuapp.com/]