import sqlite3

conn = sqlite3.connect("absensi.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM mahasiswa")

for data in cursor.fetchall():
    print(data)

conn.close()