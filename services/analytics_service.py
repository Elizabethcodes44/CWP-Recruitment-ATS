from database.database import get_connection


class AnalyticsService:

    def get_analytics(self):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            # Total candidates
            cursor.execute(
                "SELECT COUNT(*) FROM candidates"
            )
            total_candidates = cursor.fetchone()[0]

            # Total jobs
            cursor.execute(
                "SELECT COUNT(*) FROM jobs"
            )
            total_jobs = cursor.fetchone()[0]

            # Open jobs
            cursor.execute(
                "SELECT COUNT(*) FROM jobs WHERE status = ?",
                ("Open",)
            )
            open_jobs = cursor.fetchone()[0]

            # Closed jobs
            cursor.execute(
                "SELECT COUNT(*) FROM jobs WHERE status = ?",
                ("Closed",)
            )
            closed_jobs = cursor.fetchone()[0]

            # Total applications
            cursor.execute(
                "SELECT COUNT(*) FROM applications"
            )
            total_applications = cursor.fetchone()[0]

            # Applications by status
            cursor.execute(
                """
                SELECT status, COUNT(*)
                FROM applications
                GROUP BY status
                """
            )

            applications_by_status = {}

            for row in cursor.fetchall():
                applications_by_status[row[0]] = row[1]

            return {
                "total_candidates": total_candidates,
                "total_jobs": total_jobs,
                "open_jobs": open_jobs,
                "closed_jobs": closed_jobs,
                "total_applications": total_applications,
                "applications_by_status": applications_by_status
            }

        finally:
            connection.close()