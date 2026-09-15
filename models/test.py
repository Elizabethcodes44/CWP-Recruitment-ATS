from candidate import Candidate
from job import Job
from application import Application
from interview import Interview

candidate1 = Candidate(
    "Elizabeth Kujore",
    "elizabeth@example.com",
    "05551234567",
    "Sivas",
    "Python, SQL, React",
    3
)
print(candidate1)

job1 = Job(
    "Python Developer",
    "Engineering",
    "Lagos",
    300000,
    500000,
    "Open",
    "2026-09-15"
)

print(job1)

job1.validate_salary()



application1 = Application(
    1,
    2,
    "2026-09-15",
    notes="Candidate has strong Python skills"
)

print(application1)
print(application1.get_status())




interview1 = Interview(
    10,
    "2026-09-20",
    "Online",
    "Faith",
    "Candidate should prepare for technical questions"
)

print(interview1)
print(interview1.get_interview_type())