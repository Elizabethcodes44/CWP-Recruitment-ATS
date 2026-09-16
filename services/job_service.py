from database.database import get_connection
from models.job import Job


class JobService:

    # CREATE - Add a new job
    def add_job(self, job):
        job.validate_salary()

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO jobs
                (title, department, location, salary_min, salary_max, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job.title,
                    job.department,
                    job.location,
                    job.salary_min,
                    job.salary_max,
                    job.status,
                    job.created_at
                )
            )

            connection.commit()

            job.job_id = cursor.lastrowid

            return job

        finally:
            connection.close()


    # READ - Get all jobs
    def get_all_jobs(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM jobs")

            rows = cursor.fetchall()

            jobs = []

            for row in rows:
                job = Job(
                    title=row[1],
                    department=row[2],
                    location=row[3],
                    salary_min=row[4],
                    salary_max=row[5],
                    status=row[6],
                    created_at=row[7],
                    job_id=row[0]
                )

                jobs.append(job)

            return jobs

        finally:
            connection.close()


    # READ - Get one job by ID
    def get_job_by_id(self, job_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM jobs
                WHERE id = ?
                """,
                (job_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Job(
                title=row[1],
                department=row[2],
                location=row[3],
                salary_min=row[4],
                salary_max=row[5],
                status=row[6],
                created_at=row[7],
                job_id=row[0]
            )

        finally:
            connection.close()


    # UPDATE - Update an existing job
    def update_job(self, job):
        job.validate_salary()

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE jobs
                SET title = ?,
                    department = ?,
                    location = ?,
                    salary_min = ?,
                    salary_max = ?,
                    status = ?,
                    created_at = ?
                WHERE id = ?
                """,
                (
                    job.title,
                    job.department,
                    job.location,
                    job.salary_min,
                    job.salary_max,
                    job.status,
                    job.created_at,
                    job.job_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # DELETE - Delete a job
    def delete_job(self, job_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM jobs
                WHERE id = ?
                """,
                (job_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # UPDATE STATUS - Open or close a job
    def update_job_status(self, job_id, status):
        if status not in ["Open", "Closed"]:
            raise ValueError("Job status must be Open or Closed.")

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE jobs
                SET status = ?
                WHERE id = ?
                """,
                (status, job_id)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # SEARCH - Search jobs by title
    def search_by_title(self, title):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM jobs
                WHERE title LIKE ?
                """,
                (f"%{title}%",)
            )

            rows = cursor.fetchall()

            jobs = []

            for row in rows:
                job = Job(
                    title=row[1],
                    department=row[2],
                    location=row[3],
                    salary_min=row[4],
                    salary_max=row[5],
                    status=row[6],
                    created_at=row[7],
                    job_id=row[0]
                )

                jobs.append(job)

            return jobs

        finally:
            connection.close()


    # SEARCH - Search jobs by location
    def search_by_location(self, location):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM jobs
                WHERE location LIKE ?
                """,
                (f"%{location}%",)
            )

            rows = cursor.fetchall()

            jobs = []

            for row in rows:
                job = Job(
                    title=row[1],
                    department=row[2],
                    location=row[3],
                    salary_min=row[4],
                    salary_max=row[5],
                    status=row[6],
                    created_at=row[7],
                    job_id=row[0]
                )

                jobs.append(job)

            return jobs

        finally:
            connection.close()