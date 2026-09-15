import sqlite3

def get_connection():
    connection = sqlite3.connect("data/recruitment.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, email TEXT NOT NULL UNIQUE,phone TEXT, location TEXT, skills TEXT,experience_years INTEGER)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            department TEXT NOT NULL,
            location TEXT,
            salary_min REAL,
            salary_max REAL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
)""")



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_id INTEGER NOT NULL,
            job_id INTEGER NOT NULL,
            date_applied TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT,
            FOREIGN KEY (candidate_id) REFERENCES candidates(id),
            FOREIGN KEY (job_id) REFERENCES jobs(id)
);
""")


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER NOT NULL,
            interview_date TEXT NOT NULL,
            interview_type TEXT NOT NULL,
            interviewer TEXT NOT NULL,
            notes TEXT,
            FOREIGN KEY (application_id) REFERENCES applications(id)
);""")

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully")
