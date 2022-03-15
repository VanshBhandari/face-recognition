import face_recognition

image_charles = face_recognition.load_image_file('F:\programming\face recognition\image\charlesboyle.jpg')
image_bill = face_recognition.load_image_file('F:\programming\face recognition\image\bill.jpg')

charles_face_encoding = face_recognition.face_encodings(image_charles)[0]
bill_face_encoding = face_recognition.face_encodings(image_bill)[0]

face_distances = face_recognition.face_distance([charles_face_encoding], bill_face_encoding)

if face_distances <= 0.3:
  print("The 2 faces have a strong resemblence")
if 0.3< face_distances < 0.7:
  print("The 2 faces have a moderate resemblence")
if 0.7 <= face_distances:
  print("The 2 faces have little or no resemblence ")