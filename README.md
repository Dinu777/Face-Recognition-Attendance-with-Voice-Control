# Face-Recognition-Attendance-with-Voice-Control

File Structure -
    Dataset - Contains images whose face is to be Recognized 
    web - Contains all the html, css and js file for UI 
    Attendance-Intelligence.py - It is the backend
    
Run the Attendance-Intelligence.py
    - This Application has interaction with voice commands 
    - Once you hear the computer say 'Listening' wait for 3 second and say 'detect' 
    - Once you say 'detect' the system will say 'Taking Attendance' and will start detect your face
    - Once the face is detected the system will say 'Attendance Taken for {Name of the person whose face detected}' 
            => Attendance saved in Attendance Folder with date in csv format
    - Now that the attendance is taken the program will loop and will start again to listen for command 
    - If you have no more use or want to close the application say the command 'shutdown' this will shutdown the server and turn of the application 
    
    
Required python library-
  - eel
  - numpy
  - face_recognition
  - dlib
  - os
  - playsound
  - speech_recognition 
  - gTTS
  - datetime 
