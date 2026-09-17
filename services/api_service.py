import requests
from utils.logger import logger


class APIService:

    def fetch_remote_jobs(self, keyword="", title="", location=""):
        url = "https://remotive.com/api/remote-jobs"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            jobs = data.get("jobs", [])

            if keyword:
                keyword = keyword.lower()

                jobs = [
                    job for job in jobs
                    if keyword in job.get("title", "").lower()
                    or keyword in job.get("description", "").lower()
                ]

            if title:
                title = title.lower()

                jobs = [
                    job for job in jobs
                    if title in job.get("title", "").lower()
                ]

            if location:
                location = location.lower()

                jobs = [
                    job for job in jobs
                    if location in job.get(
                        "candidate_required_location", ""
                    ).lower()
                ]

            return jobs

        except requests.exceptions.RequestException as error:
            logger.error(f"External job API request failed: {error}")
            print(f"API request failed: {error}")
            return []

        except ValueError as error:
            logger.error(f"Invalid JSON received from job API: {error}")
            print("The API returned invalid data.")
            return []