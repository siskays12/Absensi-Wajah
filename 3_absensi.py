import cv2
import pandas as pd
from datetime import datetime
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml'
)

font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)

mahasiswa = {
    1: "Andi",
    2: "Budi",
    3: "Siti"
}

while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        if confidence < 70:

            nama = mahasiswa.get(
                id,
                "Unknown"
            )

            waktu = datetime.now()

            file = "absensi.csv"

            data = pd.DataFrame({
                "Nama": [nama],
                "Tanggal": [
                    waktu.strftime("%d-%m-%Y")
                ],
                "Jam": [
                    waktu.strftime("%H:%M:%S")
                ]
            })

            if not os.path.exists(file):
                data.to_csv(
                    file,
                    index=False
                )
            else:
                data.to_csv(
                    file,
                    mode='a',
                    header=False,
                    index=False
                )

            text = nama

        else:
            text = "Unknown"

        cv2.putText(
            img,
            text,
            (x, y-10),
            font,
            0.8,
            (255, 255, 255),
            2
        )

    cv2.imshow(
        'Sistem Absensi Wajah',
        img
    )

    k = cv2.waitKey(10) & 0xff

    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()