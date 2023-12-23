import os  #allows us to interact with the OS
import numpy as np
import cv2 as cv


people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'pics/Faces/train/'

features =[]        #image arrays 
labels = []         #for each face in labels, what label does it correspond to          Note:you can decalre then as numpy array here only. Commands in the function will have to change slightly

haar_cascade = cv.CascadeClassifier('Advanced/haar_face.xml') #cascade classifier will read the xml file at store it in a variable

def create_train():
    for person in people:
        path = os.path.join(DIR, person)    #going through each folder
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for x,y,w,h in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

#print(labels)
#print(f'length of feature {len(features)}')

features = np.array(features, dtype='object')

labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Training the recongnizer on features list and lables list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

