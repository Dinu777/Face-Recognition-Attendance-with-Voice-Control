# Face-Recognition-Attendance-with-Voice-Control

# UI

<img src="web/Attendance Intelligence - UI.png" alt="My cool logo"/>

# File Structure -
    Dataset - Contains images whose face is to be Recognized 
    web - Contains all the html, css and js file for UI 
    Attendance-Intelligence.py - It is the backend
    
# Run the Attendance-Intelligence.py
    1. This Application has interaction with voice commands 
    2. Once you hear the computer say 'Listening' wait for 3 second and say 'detect' 
    3. Once you say 'detect' the system will say 'Taking Attendance' and will start detect your face
    4. Once the face is detected the system will say 'Attendance Taken for {Name of the person whose face detected}' 
            -> Attendance saved in Attendance Folder with date in csv format
    5. Now that the attendance is taken the program will loop and will start again to listen for command 
    6. If you have no more use or want to close the application say the command 'shutdown' this will shutdown the server and turn of the application 
    
    
# Required python library-
  - eel
  - numpy
  - face_recognition
  - dlib
  - os
  - playsound
  - speech_recognition 
  - gTTS
  - datetime                                
 <pre>                                 
                            iiii  
                           i::::i 
                            iiii  
                                  
          aaaaaaaaaaaaa   iiiiiii 
          a::::::::::::a  i:::::i 
          aaaaaaaaa:::::a  i::::i 
                   a::::a  i::::i 
            aaaaaaa:::::a  i::::i 
          aa::::::::::::a  i::::i 
         a::::aaaa::::::a  i::::i 
        a::::a    a:::::a  i::::i 
        a::::a    a:::::a i::::::i
 ...... a:::::aaaa::::::a i::::::i
 .::::.  a::::::::::aa:::ai::::::i
 ......   aaaaaaaaaa  aaaaiiiiiiii

</pre>
