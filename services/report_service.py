import csv
from database.database import get_connection


class ReportService:

    def export_recruitment_report(self, filename="recruitment_report.csv"):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            # Get candidates
            cursor.execute("""
                SELECT id, name, email, phone, location,
                       skills, experience_years
                FROM candidates
            """)

            candidates = cursor.fetchall()

            # Get jobs
            cursor.execute("""
                SELECT id, title, department, location,
                       salary_min, salary_max, status, created_at
                FROM jobs
            """)

            jobs = cursor.fetchall()

            # Get applications
            cursor.execute("""
                SELECT id, candidate_id, job_id,
                       date_applied, status, notes
                FROM applications
            """)

            applications = cursor.fetchall()

            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                # Candidates section
                writer.writerow(["CANDIDATES"])
                writer.writerow([
                    "ID",
                    "Name",
                    "Email",
                    "Phone",
                    "Location",
                    "Skills",
                    "Experience Years"
                ])

                for candidate in candidates:
                    writer.writerow(candidate)

                writer.writerow([])

                # Jobs section
                writer.writerow(["JOBS"])
                writer.writerow([
                    "ID",
                    "Title",
                    "Department",
                    "Location",
                    "Minimum Salary",
                    "Maximum Salary",
                    "Status",
                    "Created At"
                ])

                for job in jobs:
                    writer.writerow(job)

                writer.writerow([])

                # Applications section
                writer.writerow(["APPLICATIONS"])
                writer.writerow([
                    "ID",
                    "Candidate ID",
                    "Job ID",
                    "Date Applied",
                    "Status",
                    "Notes"
                ])

                for application in applications:
                    writer.writerow(application)

            return filename

        finally:
            connection.close()