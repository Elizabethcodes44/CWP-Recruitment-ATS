from database.database import get_connection
from models.interview import Interview


class InterviewService:

    # CREATE - Schedule a new interview
    def add_interview(self, interview):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            # Check that the application exists
            cursor.execute(
                """
                SELECT id FROM applications
                WHERE id = ?
                """,
                (interview.application_id,)
            )

            if cursor.fetchone() is None:
                raise ValueError("Application does not exist.")

            cursor.execute(
                """
                INSERT INTO interviews
                (application_id, interview_date, interview_type, interviewer, notes)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    interview.application_id,
                    interview.interview_date,
                    interview.get_interview_type(),
                    interview.interviewer,
                    interview.notes
                )
            )

            connection.commit()

            interview.interview_id = cursor.lastrowid

            return interview

        finally:
            connection.close()


    # READ - Get all interviews
    def get_all_interviews(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM interviews")

            rows = cursor.fetchall()

            interviews = []

            for row in rows:
                interview = Interview(
                    application_id=row[1],
                    interview_date=row[2],
                    interview_type=row[3],
                    interviewer=row[4],
                    notes=row[5],
                    interview_id=row[0]
                )

                interviews.append(interview)

            return interviews

        finally:
            connection.close()


    # READ - Get one interview by ID
    def get_interview_by_id(self, interview_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM interviews
                WHERE id = ?
                """,
                (interview_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return Interview(
                application_id=row[1],
                interview_date=row[2],
                interview_type=row[3],
                interviewer=row[4],
                notes=row[5],
                interview_id=row[0]
            )

        finally:
            connection.close()


    # READ - Get interviews belonging to one application
    def get_interviews_by_application(self, application_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM interviews
                WHERE application_id = ?
                """,
                (application_id,)
            )

            rows = cursor.fetchall()

            interviews = []

            for row in rows:
                interview = Interview(
                    application_id=row[1],
                    interview_date=row[2],
                    interview_type=row[3],
                    interviewer=row[4],
                    notes=row[5],
                    interview_id=row[0]
                )

                interviews.append(interview)

            return interviews

        finally:
            connection.close()


    # UPDATE - Update interview information
    def update_interview(self, interview):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE interviews
                SET application_id = ?,
                    interview_date = ?,
                    interview_type = ?,
                    interviewer = ?,
                    notes = ?
                WHERE id = ?
                """,
                (
                    interview.application_id,
                    interview.interview_date,
                    interview.get_interview_type(),
                    interview.interviewer,
                    interview.notes,
                    interview.interview_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # DELETE - Delete an interview
    def delete_interview(self, interview_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM interviews
                WHERE id = ?
                """,
                (interview_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()