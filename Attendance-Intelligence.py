import face_recognition
import cv2
import numpy as np
import os
import playsound
import speech_recognition as sr
import csv
from gtts import gTTS
from speech_recognition import Recognizer
from datetime import datetime
import eel

eel.init('web')


@eel.expose
def attendance():
    WAKE = "detect"
    cancel = "cancel"
    stopListening1 = "shut down"
    stopListening2 = "shutdown"

    # variable initialization
    success = True
    dataset = 'dataset'
    images = []  # LIST CONTAINING ALL THE IMAGES
    className = []  # LIST CONTAINING ALL THE CORRESPONDING CLASS Names

    attendance_path = './attendance'
    audio_path = './audio'
    if not os.path.exists(attendance_path):
        os.makedirs(attendance_path)

    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        now = datetime.now()
        date_string = now.date()
        day, month, year = now.day, now.month, now.year
        fname = f"{day}-{month}-{year}_Attendance.csv"
        fpath = os.path.join(attendance_path, fname)

        if not os.path.exists(fpath):
            with open(os.path.join(attendance_path, fname), 'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['Name', 'date', 'Time'])

        with open(os.path.join(attendance_path, fname), 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
                print(entry)
            if name not in nameList:
                time_string = now.strftime("%H:%M:%S")
                f.writelines(f'{name},{date_string},{time_string}\n')
                print(line)
                print(name)

    def speak(text):
        tts = gTTS(text=text, lang='en')
        filename = "./audio/voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def get_audio():
        r = Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=5)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: " + str(e))

        return said.lower()

    # Reading the dataset and encoding values and objects
    myList = os.listdir(dataset)
    print("Total Classes Detected:", len(myList))

    for x, cl in enumerate(myList):
        curImg = cv2.imread(f'{dataset}/{cl}')
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])

    encodeListKnown = findEncodings(images)
    print('Encodings Complete')

    # listening for keyword
    speak("Listening")

    while success:
        print("Listening")
        text = get_audio()

        if text.count(WAKE):
            speak("Taking Attendance")
            awake = True
            cap = cv2.VideoCapture(0)

            while awake:
                success, img = cap.read()
                imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

                for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                    matchIndex = np.argmin(faceDis)

                    if matches[matchIndex]:
                        name = className[matchIndex].upper()
                        # print(name)
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        markAttendance(name)
                        speak("attendance taken for " + str(name))
                        awake = False

                cv2.imshow("attendance", img)
                cv2.waitKey(1)

            cap.release()
            cv2.destroyAllWindows()

        if text.count(stopListening1) or text.count(stopListening2):
            speak("Shutting down")
            success = False


try:
    eel.start('index.html', size=(1050, 539))

except (SystemExit, MemoryError, KeyboardInterrupt):
    pass

print('Closed browser log...!')
