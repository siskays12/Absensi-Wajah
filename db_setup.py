import sqlite3

conn = sqlite3.connect("absensi.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY,
    nim TEXT,
    nama TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS absensi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nim TEXT,
    nama TEXT,
    tanggal TEXT,
    jam TEXT
)
""")

conn.commit()
conn.close()

print("Database berhasil dibuat")