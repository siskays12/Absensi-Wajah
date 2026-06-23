import sqlite3

conn = sqlite3.connect("absensi.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

for tabel in cursor.fetchall():
    print(tabel[0])

conn.close()