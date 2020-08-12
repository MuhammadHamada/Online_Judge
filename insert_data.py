from app import APP
from models import User, Contest, Problem, Submission, Participate

"""
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

p1 = Problem(name="time square", difficulty="A", text="kkjadfkjabfja", contest_id=1)
p2 = Problem(name="space", difficulty="B", text="bvksdkbsjbvds", contest_id=1)
p3 = Problem(name="travel", difficulty="C", text="liejiejfejfii", contest_id=1)

p3 = Problem(name="smart car", difficulty="A", text="adjldnjldanldaj", contest_id=2)
p4 = Problem(name="robot", difficulty="B", text="adjbljdaldjabjda", contest_id=2)
p5 = Problem(name="holiday", difficulty="C", text="vkxkvmmkvmvkx", contest_id=2)

p6 = Problem(name="water", difficulty="A", text="dnnjdns", contest_id=3)
p7 = Problem(name="Oil", difficulty="B", text="asmccadc", contest_id=3)
p8 = Problem(name="graph", difficulty="C", text="fjkeef", contest_id=3)

p9 = Problem(name="ball", difficulty="A", text="adjldnjldanldaj", contest_id=4)
p10 = Problem(name="walls", difficulty="B", text="adjbljdaldjabjda", contest_id=4)
p11 = Problem(name="clusters", difficulty="C", text="vkxkvmmkvmvkx", contest_id=4)

p9 = Problem(name="Black Magic", difficulty="A", text="adjldnjldanldaj", contest_id=5)
p10 = Problem(name="White door", difficulty="A", text="adjbljdaldjabjda", contest_id=6)
p11 = Problem(name="station", difficulty="A", text="vkxkvmmkvmvkx", contest_id=7)

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


s1 = Submission(code="djabjfba", verdict="Wrong Answer", user_id= 1, problem_id=1)
s2 = Submission(code="SPKAWEEW", verdict="TLE", user_id= 1, problem_id=1)
s3 = Submission(code="KAJDJDFV", verdict="Accepted", user_id= 1, problem_id=1)

s4 = Submission(code="ADLJDVFV", verdict="TLE", user_id= 2, problem_id=2)
s5 = Submission(code="AJKDFVFV", verdict="Accepted", user_id= 3, problem_id=3)
s6 = Submission(code="sfklfkwr", verdict="Accepted", user_id= 4, problem_id=4)
s7 = Submission(code="sljfwfwr", verdict="Wrong Answer", user_id= 4, problem_id=5)
s8 = Submission(code="sfliffse", verdict="Accepted", user_id= 4, problem_id=6)
s9 = Submission(code="sfljfslj", verdict="Accepted", user_id= 3, problem_id=7)
s10 = Submission(code="qieqeqq", verdict="Accepted", user_id= 2, problem_id=8)
s11 = Submission(code="qlejjeq", verdict="TLE", user_id= 5, problem_id=8)
s12 = Submission(code="qeljeje", verdict="Accepted", user_id= 5, problem_id=9)
s13 = Submission(code="qejlqel", verdict="Wrong Answer", user_id= 1, problem_id=10)
s14 = Submission(code="qekejql", verdict="Accepted", user_id= 1, problem_id=11)

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



pc1 = Participate(user_id= 1, contest_id=1)
pc2 = Participate(user_id= 1, contest_id=2)
pc3 = Participate(user_id= 1, contest_id=7)
pc4 = Participate(user_id= 2, contest_id=2)
pc5 = Participate(user_id= 2, contest_id=3)
pc6 = Participate(user_id= 2, contest_id=7)
pc7 = Participate(user_id= 3, contest_id=7)
pc8 = Participate(user_id= 4, contest_id=1)
pc9 = Participate(user_id= 4, contest_id=3)
pc10 = Participate(user_id= 4, contest_id=4)
pc11 = Participate(user_id= 4, contest_id=5)
pc12 = Participate(user_id= 5, contest_id=3)

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


"""