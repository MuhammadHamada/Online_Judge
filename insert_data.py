from app import app
from models import User, Contest, Problem, Submission, Participate


Participate.query.delete()
Submission.query.delete()
Problem.query.delete()
User.query.delete()
Contest.query.delete()

user1 = User(handle="hamada", rating=1056, level="newbie")
user2 = User(handle="mohamed", rating=1201, level="pupil")
user3 = User(handle="omar", rating=1401, level="specialist")
user4 = User(handle="ahmed", rating=1660, level="expert")
user5 = User(handle="dawod", rating=1200, level="master")

user1.insert()
user2.insert()
user3.insert()
user4.insert()
user5.insert()


contest1 = Contest(name="Codeforces Round #1", divison=1)
contest2 = Contest(name="Codeforces Round #2", divison=1)
contest3 = Contest(name="Codeforces Round #3", divison=2)
contest4 = Contest(name="Codeforces Round #4", divison=3)
contest5 = Contest(name="Educational Round #1", divison=2)
contest6 = Contest(name="Educational Round #2", divison=3)
contest7 = Contest(name="Global Round #1", divison=0)

contest1.insert()
contest2.insert()
contest3.insert()
contest4.insert()
contest5.insert()
contest6.insert()
contest7.insert()


p1 = Problem(
    name="time square",
    difficulty="A",
    text="kkjadfkjabfja",
    contest_id=contest1.id)
p2 = Problem(
    name="space",
    difficulty="B",
    text="bvksdkbsjbvds",
    contest_id=contest1.id)
p3 = Problem(
    name="travel",
    difficulty="C",
    text="liejiejfejfii",
    contest_id=contest1.id)

p3 = Problem(
    name="smart car",
    difficulty="A",
    text="adjldnjldanldaj",
    contest_id=contest2.id)
p4 = Problem(
    name="robot",
    difficulty="B",
    text="adjbljdaldjabjda",
    contest_id=contest2.id)
p5 = Problem(
    name="holiday",
    difficulty="C",
    text="vkxkvmmkvmvkx",
    contest_id=contest2.id)

p6 = Problem(
    name="water",
    difficulty="A",
    text="dnnjdns",
    contest_id=contest3.id)
p7 = Problem(
    name="Oil",
    difficulty="B",
    text="asmccadc",
    contest_id=contest3.id)
p8 = Problem(
    name="graph",
    difficulty="C",
    text="fjkeef",
    contest_id=contest3.id)

p9 = Problem(
    name="ball",
    difficulty="A",
    text="adjldnjldanldaj",
    contest_id=contest4.id)
p10 = Problem(
    name="walls",
    difficulty="B",
    text="adjbljdaldjabjda",
    contest_id=contest4.id)
p11 = Problem(
    name="clusters",
    difficulty="C",
    text="vkxkvmmkvmvkx",
    contest_id=contest4.id)

p9 = Problem(
    name="Black Magic",
    difficulty="A",
    text="adjldnjldanldaj",
    contest_id=contest5.id)
p10 = Problem(
    name="White door",
    difficulty="A",
    text="adjbljdaldjabjda",
    contest_id=contest6.id)
p11 = Problem(
    name="station",
    difficulty="A",
    text="vkxkvmmkvmvkx",
    contest_id=contest7.id)

p1.insert()
p2.insert()
p3.insert()
p4.insert()
p5.insert()
p6.insert()
p7.insert()
p8.insert()
p9.insert()
p10.insert()
p11.insert()


s1 = Submission(
    code="djabjfba",
    verdict="Wrong Answer",
    user_id=user1.id,
    problem_id=p1.id)
s2 = Submission(
    code="SPKAWEEW",
    verdict="TLE",
    user_id=user1.id,
    problem_id=p1.id)
s3 = Submission(
    code="KAJDJDFV",
    verdict="Accepted",
    user_id=user1.id,
    problem_id=p1.id)

s4 = Submission(
    code="ADLJDVFV",
    verdict="TLE",
    user_id=user2.id,
    problem_id=p2.id)
s5 = Submission(
    code="AJKDFVFV",
    verdict="Accepted",
    user_id=user3.id,
    problem_id=p3.id)
s6 = Submission(
    code="sfklfkwr",
    verdict="Accepted",
    user_id=user4.id,
    problem_id=p4.id)
s7 = Submission(
    code="sljfwfwr",
    verdict="Wrong Answer",
    user_id=user4.id,
    problem_id=p5.id)
s8 = Submission(
    code="sfliffse",
    verdict="Accepted",
    user_id=user4.id,
    problem_id=p6.id)
s9 = Submission(
    code="sfljfslj",
    verdict="Accepted",
    user_id=user3.id,
    problem_id=p7.id)
s10 = Submission(
    code="qieqeqq",
    verdict="Accepted",
    user_id=user2.id,
    problem_id=p8.id)
s11 = Submission(
    code="qlejjeq",
    verdict="TLE",
    user_id=user5.id,
    problem_id=p8.id)
s12 = Submission(
    code="qeljeje",
    verdict="Accepted",
    user_id=user5.id,
    problem_id=p9.id)
s13 = Submission(
    code="qejlqel",
    verdict="Wrong Answer",
    user_id=user1.id,
    problem_id=p10.id)
s14 = Submission(
    code="qekejql",
    verdict="Accepted",
    user_id=user1.id,
    problem_id=p11.id)

s1.insert()
s2.insert()
s3.insert()
s4.insert()
s5.insert()
s6.insert()
s7.insert()
s8.insert()
s9.insert()
s10.insert()
s11.insert()
s12.insert()
s13.insert()
s14.insert()


pc1 = Participate(user_id=user1.id, contest_id=contest1.id)
pc2 = Participate(user_id=user1.id, contest_id=contest2.id)
pc3 = Participate(user_id=user1.id, contest_id=contest7.id)
pc4 = Participate(user_id=user2.id, contest_id=contest2.id)
pc5 = Participate(user_id=user2.id, contest_id=contest3.id)
pc6 = Participate(user_id=user2.id, contest_id=contest7.id)
pc7 = Participate(user_id=user3.id, contest_id=contest7.id)
pc8 = Participate(user_id=user4.id, contest_id=contest1.id)
pc9 = Participate(user_id=user4.id, contest_id=contest3.id)
pc10 = Participate(user_id=user4.id, contest_id=contest4.id)
pc11 = Participate(user_id=user4.id, contest_id=contest5.id)
pc12 = Participate(user_id=user5.id, contest_id=contest3.id)

pc1.insert()
pc2.insert()
pc3.insert()
pc4.insert()
pc5.insert()
pc6.insert()
pc7.insert()
pc8.insert()
pc9.insert()
pc10.insert()
pc11.insert()
pc12.insert()
