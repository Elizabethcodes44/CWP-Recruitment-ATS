from models.candidate import Candidate
from models.job import Job
from models.application import Application
from models.interview import Interview

from services.candidate_service import CandidateService
from services.job_service import JobService
from services.application_service import ApplicationService
from services.interview_service import InterviewService

from database.database import create_tables

from datetime import datetime

candidate_service = CandidateService()
job_service = JobService()
application_service = ApplicationService()
interview_service = InterviewService()

def add_candidate():
    print("\n--- ADD CANDIDATE ---")

    try:
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        location = input("Location: ").strip()
        skills = input("Skills: ").strip()

        experience_years = int(
            input("Years of experience: ")
        )

        candidate = Candidate(
            name,
            email,
            phone,
            location,
            skills,
            experience_years
        )

        saved_candidate = candidate_service.add_candidate(candidate)

        print(
            f"\nCandidate added successfully. "
            f"ID: {saved_candidate.candidate_id}"
        )

    except ValueError as error:
        print("Error:", error)

def add_job():
    print("\n--- ADD JOB ---")

    try:
        title = input("Job title: ").strip()
        department = input("Department: ").strip()
        location = input("Location: ").strip()

        salary_min = float(
            input("Minimum salary: ")
        )

        salary_max = float(
            input("Maximum salary: ")
        )

        status = input(
            "Status (Open/Closed): "
        ).strip().title()

        if status not in ["Open", "Closed"]:
            raise ValueError("Status must be Open or Closed.")

        created_at = datetime.now().strftime("%Y-%m-%d")

        job = Job(
            title,
            department,
            location,
            salary_min,
            salary_max,
            status,
            created_at
        )

        saved_job = job_service.add_job(job)

        print(
            f"\nJob added successfully. "
            f"ID: {saved_job.job_id}"
        )

    except ValueError as error:
        print("Error:", error)

def apply_candidate_to_job():
    print("\n--- APPLY CANDIDATE TO JOB ---")

    try:
        candidate_id = int(
            input("Candidate ID: ")
        )

        job_id = int(
            input("Job ID: ")
        )

        notes = input(
            "Application notes (optional): "
        ).strip()

        date_applied = datetime.now().strftime("%Y-%m-%d")

        application = Application(
            candidate_id=candidate_id,
            job_id=job_id,
            date_applied=date_applied,
            status="Applied",
            notes=notes if notes else None
        )

        saved_application = application_service.add_application(
            application
        )

        print(
            f"\nApplication created successfully. "
            f"ID: {saved_application.application_id}"
        )

    except ValueError as error:
        print("Error:", error)

def update_application_status():
    print("\n--- UPDATE APPLICATION STATUS ---")

    try:
        application_id = int(
            input("Application ID: ")
        )

        print("\nAvailable statuses:")

        for status in Application.VALID_STATUSES:
            print("-", status)

        new_status = input(
            "\nNew status: "
        ).strip()

        updated = application_service.update_status(
            application_id,
            new_status
        )

        if updated:
            print("Application status updated successfully.")
        else:
            print("Application not found.")

    except ValueError as error:
        print("Error:", error)

def schedule_interview():
    print("\n--- SCHEDULE INTERVIEW ---")

    try:
        application_id = int(
            input("Application ID: ")
        )

        interview_date = input(
            "Interview date (YYYY-MM-DD): "
        ).strip()

        print("\nInterview types:")

        for interview_type in Interview.VALID_TYPES:
            print("-", interview_type)

        interview_type = input(
            "\nInterview type: "
        ).strip()

        interviewer = input(
            "Interviewer name: "
        ).strip()

        notes = input(
            "Notes (optional): "
        ).strip()

        interview = Interview(
            application_id=application_id,
            interview_date=interview_date,
            interview_type=interview_type,
            interviewer=interviewer,
            notes=notes if notes else None
        )

        saved_interview = interview_service.add_interview(
            interview
        )

        print(
            f"\nInterview scheduled successfully. "
            f"ID: {saved_interview.interview_id}"
        )

    except ValueError as error:
        print("Error:", error)

def search_candidates():
    print("\n--- SEARCH CANDIDATES ---")

    print("1. Search by name")
    print("2. Search by skill")

    choice = input("Choose search type: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        results = candidate_service.search_by_name(name)

    elif choice == "2":
        skill = input("Enter skill: ").strip()
        results = candidate_service.search_by_skill(skill)

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No candidates found.")
        return

    print("\nResults:")

    for candidate in results:
        print(candidate)

def search_jobs():
    print("\n--- SEARCH JOBS ---")

    print("1. Search by title")
    print("2. Search by location")

    choice = input("Choose search type: ").strip()

    if choice == "1":
        title = input("Enter job title: ").strip()
        results = job_service.search_by_title(title)

    elif choice == "2":
        location = input("Enter location: ").strip()
        results = job_service.search_by_location(location)

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No jobs found.")
        return

    print("\nResults:")

    for job in results:
        print(job)

def view_applications():
    print("\n--- APPLICATIONS ---")

    applications = application_service.get_all_applications()

    if not applications:
        print("No applications found.")
        return

    for application in applications:
        print(application)

def change_job_status():
    print("\n--- CHANGE JOB STATUS ---")

    try:
        job_id = int(
            input("Job ID: ")
        )

        status = input(
            "New status (Open/Closed): "
        ).strip().title()

        updated = job_service.update_job_status(
            job_id,
            status
        )

        if updated:
            print("Job status updated successfully.")
        else:
            print("Job not found.")

    except ValueError as error:
        print("Error:", error)

def main():
    create_tables()

    while True:
        print("\n==============================")
        print("     RECRUITMENT ATS")
        print("==============================")

        print("1. Add Candidate")
        print("2. Add Job")
        print("3. Apply Candidate to Job")
        print("4. Update Application Status")
        print("5. Schedule Interview")
        print("6. Search Candidates")
        print("7. Search Jobs")
        print("8. View Applications")
        print("9. Change Job Status")
        print("10. View Analytics")
        print("11. Export Report")
        print("12. Fetch API Data")
        print("13. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_candidate()

        elif choice == "2":
            add_job()

        elif choice == "3":
            apply_candidate_to_job()

        elif choice == "4":
            update_application_status()

        elif choice == "5":
            schedule_interview()

        elif choice == "6":
            search_candidates()

        elif choice == "7":
            search_jobs()

        elif choice == "8":
            view_applications()

        elif choice == "9":
            change_job_status()

        elif choice == "10":
            print("Analytics will be integrated here.")

        elif choice == "11":
            print("Report export will be integrated here.")

        elif choice == "12":
            print("API integration will be added here.")

        elif choice == "13":
            print("\nThank you for using Recruitment ATS.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()