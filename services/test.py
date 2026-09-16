from models.candidate import Candidate
from services.candidate_service import CandidateService

from models.job import Job
from services.job_service import JobService

from models.application import Application
from services.application_service import ApplicationService

service = CandidateService()


# CREATE
candidate = Candidate(
    "Elizabeth Test 4",
    "elizabethtest4@example.com",
    "05551234567",
    "Sivas",
    "Python, React, mySQL",
    2
)

saved_candidate = service.add_candidate(candidate)

print("Candidate created:")
print(saved_candidate)
print("Candidate ID:", saved_candidate.candidate_id)

job_service = JobService()

job = Job(
    "Python Developer",
    "Engineering",
    "Lagos",
    300000,
    500000,
    "Open",
    "2026-09-16"
)

saved_job = job_service.add_job(job)

print("Job created:")
print(saved_job)
print("Job ID:", saved_job.job_id)




application_service = ApplicationService()



application = Application(
    candidate_id=2,
    job_id=1,
    date_applied="2026-09-16"
)

application_service.add_application(application)

saved_application = application_service.add_application(application)


print("Application created:")
print(saved_application)
print("Application ID:", saved_application.application_id)