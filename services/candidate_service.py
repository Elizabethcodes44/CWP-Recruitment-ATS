from database.database import get_connection
from models.candidate import Candidate
import sqlite3


class CandidateService:

    # CREATE - Add a new candidate
    def add_candidate(self, candidate):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO candidates
                (name, email, phone, location, skills, experience_years)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    candidate.name,
                    candidate.email,
                    candidate.phone,
                    candidate.location,
                    candidate.skills,
                    candidate.get_experience_years()
                )
            )

            connection.commit()

            candidate.candidate_id = cursor.lastrowid

            return candidate

        except sqlite3.IntegrityError:
            raise ValueError(
                "A candidate with this email already exists."
            )

        finally:
            connection.close()


    # READ - Get all candidates
    def get_all_candidates(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM candidates")

            rows = cursor.fetchall()

            candidates = []

            for row in rows:
                candidate = Candidate(
                    name=row[1],
                    email=row[2],
                    phone=row[3],
                    location=row[4],
                    skills=row[5],
                    experience_years=row[6],
                    candidate_id=row[0]
                )

                candidates.append(candidate)

            return candidates

        finally:
            connection.close()


    # READ - Get one candidate using ID
    def get_candidate_by_id(self, candidate_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM candidates
                WHERE id = ?
                """,
                (candidate_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            candidate = Candidate(
                name=row[1],
                email=row[2],
                phone=row[3],
                location=row[4],
                skills=row[5],
                experience_years=row[6],
                candidate_id=row[0]
            )

            return candidate

        finally:
            connection.close()


    # UPDATE - Update an existing candidate
    def update_candidate(self, candidate):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE candidates
                SET name = ?,
                    email = ?,
                    phone = ?,
                    location = ?,
                    skills = ?,
                    experience_years = ?
                WHERE id = ?
                """,
                (
                    candidate.name,
                    candidate.email,
                    candidate.phone,
                    candidate.location,
                    candidate.skills,
                    candidate.get_experience_years(),
                    candidate.candidate_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except sqlite3.IntegrityError:
            raise ValueError(
                "A candidate with this email already exists."
            )

        finally:
            connection.close()


    # DELETE - Delete candidate using ID
    def delete_candidate(self, candidate_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM candidates
                WHERE id = ?
                """,
                (candidate_id,)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()


    # SEARCH - Search candidate by name
    def search_by_name(self, name):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM candidates
                WHERE name LIKE ?
                """,
                (f"%{name}%",)
            )

            rows = cursor.fetchall()

            candidates = []

            for row in rows:
                candidate = Candidate(
                    name=row[1],
                    email=row[2],
                    phone=row[3],
                    location=row[4],
                    skills=row[5],
                    experience_years=row[6],
                    candidate_id=row[0]
                )

                candidates.append(candidate)

            return candidates

        finally:
            connection.close()


    # SEARCH - Search candidate by skill
    def search_by_skill(self, skill):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM candidates
                WHERE skills LIKE ?
                """,
                (f"%{skill}%",)
            )

            rows = cursor.fetchall()

            candidates = []

            for row in rows:
                candidate = Candidate(
                    name=row[1],
                    email=row[2],
                    phone=row[3],
                    location=row[4],
                    skills=row[5],
                    experience_years=row[6],
                    candidate_id=row[0]
                )

                candidates.append(candidate)

            return candidates

        finally:
            connection.close()