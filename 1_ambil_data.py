import cv2
import os

# 1. Aktifkan Kamera utama (angka 0)
kamera = cv2.VideoCapture(0)

# 2. Panggil detektor wajah Haar Cascade yang sudah diunduh
deteksi_wajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 3. Input ID Mahasiswa (Harus berupa ANGKA, misal: 1, 2, 3)
student_id = input("Masukkan ID / NIM Mahasiswa (Angka saja): ")
print("Kamera terbuka. Silakan melihat ke kamera...")

hitung = 0

while True:
    # Ambil frame dari kamera
    ret, frame = kamera.read()
    
    # Ubah warna gambar ke keabuan (wajib untuk Haar Cascade)
    bukan_warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Cari wajah di dalam gambar
    daftar_wajah = deteksi_wajah.detectMultiScale(bukan_warna, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in daftar_wajah:
        hitung += 1
        
        # Potong gambar hanya di bagian wajah, lalu simpan ke folder 'dataset'
        # Nama file: User.[ID_Mahasiswa].[Nomor_Foto].jpg
        nama_file = f"dataset/User.{student_id}.{hitung}.jpg"
        cv2.imwrite(nama_file, bukan_warna[y:y+h, x:x+w])
        
        # Gambar kotak hijau di layar sebagai penanda wajah terdeteksi
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Tampilkan video rekaman di layar komputer
    cv2.imshow('Proses Pengambilan Wajah', frame)

    # Berhenti otomatis jika foto sudah terkumpul 30, atau jika menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q') or hitung >= 30:
        break

print(f"Selesai! 30 gambar wajah telah disimpan untuk ID {student_id}.")
kamera.release()
cv2.destroyAllWindows()