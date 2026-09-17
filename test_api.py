# import requests

# url = "https://remotive.com/api/remote-jobs"

# response = requests.get(url)
# print(response.status_code)

# data = response.json()

# import requests

# url = "https://remotive.com/api/remote-jobs"

# response = requests.get(url)

# data = response.json()

# jobs = data["jobs"]

# for job in jobs:
#     print("------------------------------")
#     print("Job Title:", job["title"])
#     print("Company:", job["company_name"])
#     print("Location:", job["candidate_required_location"])
#     print("Job Type:", job["job_type"])
#     print("Salary:", job["salary"])
#     print("URL:", job["url"])

from services.api_service import APIService


api_service = APIService()

jobs = api_service.fetch_remote_jobs(
    keyword="python",
    location="Canada"
)

print(f"Found {len(jobs)} jobs.\n")

for job in jobs[:5]:
    print("Title:", job.get("title"))
    print("Company:", job.get("company_name"))
    print("Location:", job.get("candidate_required_location"))
    print("URL:", job.get("url"))
    print("-" * 50)