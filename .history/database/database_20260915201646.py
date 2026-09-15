import sqlite3

connection = sqlite3.connect("data/recruitment.db")

print("Database connected successfully")

cursor = connection.cursor()

cursor.execute