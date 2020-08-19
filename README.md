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
- get the data of all users
- Request : GET https://ojudge.herokuapp.com/users
- Request Arguments : None
- Response :
```
{
    "success": true,
    "total_users": 5,
    "users": [
        {
            "handle": "hamada",
            "id": 8,
            "level": "newbie",
            "rating": 1056
        },
        {
            "handle": "mohamed",
            "id": 9,
            "level": "pupil",
            "rating": 1201
        },
        {
            "handle": "omar",
            "id": 10,
            "level": "specialist",
            "rating": 1401
        },
        {
            "handle": "ahmed",
            "id": 11,
            "level": "expert",
            "rating": 1660
        },
        {
            "handle": "dawod",
            "id": 12,
            "level": "master",
            "rating": 1200
        }
    ]
}
```

#### POST /users
- create new user
- Request : POST https://ojudge.herokuapp.com/users
- Request Arguments :
```
{
    "handle": "Momentum",
    "rating": 1200,
    "level" : "pupil"
}
```
- Response :
```
{
    "success": true,
    "user_id": 20
}
```

#### PATCH /users/<int:user_id>
- update the information of a specific user
- Request : PATCH https://ojudge.herokuapp.com/users/20
- Request Arguments :
```
{
    "rating": 1600,
    "level" : "expert"
}
```
- Response :
```
{
    "success": true,
    "user": {
        "handle": "Momentum",
        "id": 20,
        "level": "expert",
        "rating": 1600
    }
}
```

#### DELETE /users/<int:user_id>
- delete a specific user
- Request : DELETE https://ojudge.herokuapp.com/users/20
- Request Arguments : None
- Response :
```
{
    "deleted": 20,
    "success": true
}
```

#### GET /contests
- get all contests
- Request : GET https://ojudge.herokuapp.com/contests
- Request Arguments : None
- Response :
```
{
    "contests": [
        {
            "divison": 1,
            "id": 11,
            "name": "Codeforces Round #1",
            "time": null
        },
        {
            "divison": 1,
            "id": 12,
            "name": "Codeforces Round #2",
            "time": null
        },
        {
            "divison": 2,
            "id": 13,
            "name": "Codeforces Round #3",
            "time": null
        },
        {
            "divison": 3,
            "id": 14,
            "name": "Codeforces Round #4",
            "time": null
        },
        {
            "divison": 2,
            "id": 15,
            "name": "Educational Round #1",
            "time": null
        },
        {
            "divison": 3,
            "id": 16,
            "name": "Educational Round #2",
            "time": null
        },
        {
            "divison": 0,
            "id": 17,
            "name": "Global Round #1",
            "time": null
        }
    ],
    "success": true,
    "total_contests": 7
}
```

#### GET /contests/<int:contest_id>/users
- get handles of all user participated in a specific contest
- Request : GET https://ojudge.herokuapp.com/contests/11/users
- Request Arguments : None
- Response :
```
{
    "handles": [
        "hamada",
        "ahmed"
    ],
    "success": true
}
```

#### POST /contests
- create new contest
- Request : POST https://ojudge.herokuapp.com/contests
- Request Arguments :
```
{
    "name": "Educational Round #4",
    "divison": 2 ,
    "time" : null

}
```
- Response :
```
{
    "contest_id": 28,
    "success": true
}
```

#### PATCH /contests/<int:contest_id>
- update the information of a specific contest
- Request : PATCH https://ojudge.herokuapp.com/contests/28
- Request Arguments :
```
{
    "name": "educational Round #4",
    "divison": 3

}
```
- Response :
```
{
    "contest": {
        "divison": 3,
        "id": 28,
        "name": "educational Round #4",
        "time": null
    },
    "success": true
}
```

#### DELETE /contests/<int:contest_id>
- delete a specific contest
- Request : DELETE https://ojudge.herokuapp.com/contests/28
- Request Arguments : None
- Response :
```
{
    "deleted": 28,
    "success": true
}
```

#### GET /problems
- get all problems
- Request : GET https://ojudge.herokuapp.com/problems
- Request Arguments : None
- Response :
```
{
    "problems": [
        {
            "contest_id": 11,
            "difficulty": "A",
            "id": 5,
            "name": "time square",
            "text": "kkjadfkjabfja"
        },
        {
            "contest_id": 11,
            "difficulty": "B",
            "id": 6,
            "name": "space",
            "text": "bvksdkbsjbvds"
        },
        {
            "contest_id": 12,
            "difficulty": "A",
            "id": 7,
            "name": "smart car",
            "text": "adjldnjldanldaj"
        },
        {
            "contest_id": 12,
            "difficulty": "B",
            "id": 8,
            "name": "robot",
            "text": "adjbljdaldjabjda"
        },
        {
            "contest_id": 12,
            "difficulty": "C",
            "id": 9,
            "name": "holiday",
            "text": "vkxkvmmkvmvkx"
        },
        {
            "contest_id": 13,
            "difficulty": "A",
            "id": 10,
            "name": "water",
            "text": "dnnjdns"
        },
        {
            "contest_id": 13,
            "difficulty": "B",
            "id": 11,
            "name": "Oil",
            "text": "asmccadc"
        },
        {
            "contest_id": 13,
            "difficulty": "C",
            "id": 12,
            "name": "graph",
            "text": "fjkeef"
        },
        {
            "contest_id": 15,
            "difficulty": "A",
            "id": 13,
            "name": "Black Magic",
            "text": "adjldnjldanldaj"
        },
        {
            "contest_id": 16,
            "difficulty": "A",
            "id": 14,
            "name": "White door",
            "text": "adjbljdaldjabjda"
        },
        {
            "contest_id": 17,
            "difficulty": "A",
            "id": 15,
            "name": "station",
            "text": "vkxkvmmkvmvkx"
        }
    ],
    "success": true,
    "total_problems": 11
}
```

#### GET /contests/<int:contest_id>/problems
- get all problems of a specific contest
- Request : GET https://ojudge.herokuapp.com/contests/11/problems
- Request Arguments : None
- Response :
```
{
    "contest_id": 11,
    "problems": [
        {
            "contest_id": 11,
            "difficulty": "A",
            "id": 5,
            "name": "time square",
            "text": "kkjadfkjabfja"
        },
        {
            "contest_id": 11,
            "difficulty": "B",
            "id": 6,
            "name": "space",
            "text": "bvksdkbsjbvds"
        }
    ],
    "success": true,
    "total_problems": 2
}
```

#### POST /problems
- create new problem
- Request : POST https://ojudge.herokuapp.com/problems
- Request Arguments : 
```
{
    "name" : "Watermelon",
    "difficulty": "A" ,
    "text": "sjadnjnadjlnd",
    "contest_id" : 11
}
```
- Response :
```
{
    "problem_id": 21,
    "success": true
}
```

#### DELETE /problems/<int:problem_id>
- delete a specific problem
- Request : DELETE https://ojudge.herokuapp.com/problems/21
- Request Arguments : None
- Response :
```
{
    "deleted": 21,
    "success": true
}
```

#### GET /submissions
- get all submissions
- Request : GET https://ojudge.herokuapp.com/submissions
- Request Arguments : None
- Response :
```
{
    "submissions": [
        {
            "code": "djabjfba",
            "id": 2,
            "problem_id": 5,
            "user_id": 8,
            "verdict": "Wrong Answer"
        },
        {
            "code": "SPKAWEEW",
            "id": 3,
            "problem_id": 5,
            "user_id": 8,
            "verdict": "TLE"
        },
        {
            "code": "KAJDJDFV",
            "id": 4,
            "problem_id": 5,
            "user_id": 8,
            "verdict": "Accepted"
        },
        {
            "code": "ADLJDVFV",
            "id": 5,
            "problem_id": 6,
            "user_id": 9,
            "verdict": "TLE"
        },
        {
            "code": "AJKDFVFV",
            "id": 6,
            "problem_id": 7,
            "user_id": 10,
            "verdict": "Accepted"
        },
        {
            "code": "sfklfkwr",
            "id": 7,
            "problem_id": 8,
            "user_id": 11,
            "verdict": "Accepted"
        },
        {
            "code": "sljfwfwr",
            "id": 8,
            "problem_id": 9,
            "user_id": 11,
            "verdict": "Wrong Answer"
        },
        {
            "code": "sfliffse",
            "id": 9,
            "problem_id": 10,
            "user_id": 11,
            "verdict": "Accepted"
        },
        {
            "code": "sfljfslj",
            "id": 10,
            "problem_id": 11,
            "user_id": 10,
            "verdict": "Accepted"
        },
        {
            "code": "qieqeqq",
            "id": 11,
            "problem_id": 12,
            "user_id": 9,
            "verdict": "Accepted"
        },
        {
            "code": "qlejjeq",
            "id": 12,
            "problem_id": 12,
            "user_id": 12,
            "verdict": "TLE"
        },
        {
            "code": "qeljeje",
            "id": 13,
            "problem_id": 13,
            "user_id": 12,
            "verdict": "Accepted"
        },
        {
            "code": "qejlqel",
            "id": 14,
            "problem_id": 14,
            "user_id": 8,
            "verdict": "Wrong Answer"
        },
        {
            "code": "qekejql",
            "id": 15,
            "problem_id": 15,
            "user_id": 8,
            "verdict": "Accepted"
        }
    ],
    "success": true,
    "total_submissions": 14
}
```

#### GET /submissions/<int:problem_id>
- get all submissions of a specific problem
- Request : GET https://ojudge.herokuapp.com/submissions/5
- Request Arguments : None
- Response :
```
{
    "problem_id": 5,
    "submissions": [
        {
            "code": "djabjfba",
            "id": 2,
            "problem_id": 5,
            "user_id": 8,
            "verdict": "Wrong Answer"
        },
        {
            "code": "SPKAWEEW",
            "id": 3,
            "problem_id": 5,
            "user_id": 8,
            "verdict": "TLE"
        },
        {
            "code": "KAJDJDFV",
            "id": 4,
            "problem_id": 5,
            "user_id": 8,
            "verdict": "Accepted"
        }
    ],
    "success": true,
    "total_submissions": 3
}
```

#### POST /submissions
- create a new submission
- Request : POST https://ojudge.herokuapp.com/submissions
- Request Arguments : 
```
{
    "code" : "print(hello world)",
    "verdict": "Accepted" ,
    "user_id": 8,
    "problem_id" : 5
}
```
- Response :
```
{
    "submission_id": 17,
    "success": true
}
```
#### GET /participations
- get all participations
- Request : GET https://ojudge.herokuapp.com/participations
- Request Arguments : None
- Response :
```
{
    "participations": [
        {
            "contest_id": 11,
            "id": 2,
            "user_id": 8
        },
        {
            "contest_id": 12,
            "id": 3,
            "user_id": 8
        },
        {
            "contest_id": 17,
            "id": 4,
            "user_id": 8
        },
        {
            "contest_id": 12,
            "id": 5,
            "user_id": 9
        },
        {
            "contest_id": 13,
            "id": 6,
            "user_id": 9
        },
        {
            "contest_id": 17,
            "id": 7,
            "user_id": 9
        },
        {
            "contest_id": 17,
            "id": 8,
            "user_id": 10
        },
        {
            "contest_id": 11,
            "id": 9,
            "user_id": 11
        },
        {
            "contest_id": 13,
            "id": 10,
            "user_id": 11
        },
        {
            "contest_id": 14,
            "id": 11,
            "user_id": 11
        },
        {
            "contest_id": 15,
            "id": 12,
            "user_id": 11
        },
        {
            "contest_id": 13,
            "id": 13,
            "user_id": 12
        }
    ],
    "success": true,
    "total_participations": 12
}
```
#### POST /participate
- participate in a specific contest
- Request : POST https://ojudge.herokuapp.com/participate
- Request Arguments : 
```
{
    "user_id" : 11,
    "contest_id" : 17
}
```
- Response :
```
{
    "paticipation_id": 15,
    "success": true
}
```