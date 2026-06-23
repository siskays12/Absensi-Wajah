import sqlite3

conn = sqlite3.connect("absensi.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO mahasiswa (id,nim,nama)
VALUES (1,'240658302004','Siska')
""")

conn.commit()
conn.close()

print("Data mahasiswa berhasil ditambahkan")