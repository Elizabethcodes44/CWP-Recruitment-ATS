from database.database import get_connection
from models.application import Application


class ApplicationService:

    # CREATE - Candidate applies for a job
    def add_application(self, application):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            # Check that the candidate exists
            cursor.execute(
                "SELECT id FROM candidates WHERE id = ?",
                (application.candidate_id,)
            )

            if cursor.fetchone() is None:
                raise ValueError("Candidate does not exist.")

            # Check that the job exists
            cursor.execute(
                "SELECT id FROM jobs WHERE id = ?",
                (application.job_id,)
            )

            if cursor.fetchone() is None:
                raise ValueError("Job does not exist.")

            cursor.execute(
                """
                INSERT INTO applications
                (candidate_id, job_id, date_applied, status, notes)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    application.candidate_id,
                    application.job_id,
                    application.date_applied,
                    application.get_status(),
                    application.notes
                )
            )

            connection.commit()

            application.application_id = cursor.lastrowid

            return application

        finally:
            connection.close()


    # READ - Get all applications
    def get_all_applications(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM applications")

            rows = cursor.fetchall()

            applications = []

            for row in rows:
                application = Application(
                    candidate_id=row[1],
                    job_id=row[2],
                    date_applied=row[3],
                    status=row[4],
                    notes=row[5],
                    application_id=row[0]
                )

                applications.append(application)

            return applications

        finally:
            connection.close()


    # READ - Get one application by ID
    def get_application_by_id(self, application_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM applications
                WHERE id = ?
                """,
                (application_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Application(
                candidate_id=row[1],
                job_id=row[2],
                date_applied=row[3],
                status=row[4],
                notes=row[5],
                application_id=row[0]
            )

        finally:
            connection.close()


    # UPDATE - Update the whole application
    def update_application(self, application):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE applications
                SET candidate_id = ?,
                    job_id = ?,
                    date_applied = ?,
                    status = ?,
                    notes = ?
                WHERE id = ?
                """,
                (
                    application.candidate_id,
                    application.job_id,
                    application.date_applied,
                    application.get_status(),
                    application.notes,
                    application.application_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # UPDATE - Change only application status
    def update_status(self, application_id, new_status):
        # Use the model to validate the status
        if new_status not in Application.VALID_STATUSES:
            raise ValueError(
                f"Invalid application status: {new_status}"
            )

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE applications
                SET status = ?
                WHERE id = ?
                """,
                (new_status, application_id)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # UPDATE - Change application notes
    def update_notes(self, application_id, notes):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE applications
                SET notes = ?
                WHERE id = ?
                """,
                (notes, application_id)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # DELETE
    def delete_application(self, application_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM applications
                WHERE id = ?
                """,
                (application_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # SEARCH/FILTER - Find applications by status
    def search_by_status(self, status):
        if status not in Application.VALID_STATUSES:
            raise ValueError(
                f"Invalid application status: {status}"
            )

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM applications
                WHERE status = ?
                """,
                (status,)
            )

            rows = cursor.fetchall()

            applications = []

            for row in rows:
                application = Application(
                    candidate_id=row[1],
                    job_id=row[2],
                    date_applied=row[3],
                    status=row[4],
                    notes=row[5],
                    application_id=row[0]
                )

                applications.append(application)

            return applications

        finally:
            connection.close()