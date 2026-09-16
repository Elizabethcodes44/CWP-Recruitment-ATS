from models.candidate import Candidate
from services.candidate_service import CandidateService
from models.job import Job
from services.job_service import JobService

service = CandidateService()


# CREATE
candidate = Candidate(
    "Elizabeth Test 2",
    "elizabethtest2@example.com",
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