import face_recognition
from PIL import Image

image = face_recognition.load_image_file('F:\programming\face recognition\image\rickastley.png')
face_location = face_recognition.face_locations(image)

print(f'Number of people in this image: {len(face_location)}')

for i in face_location:
  top, right, bottom, left = i
  face_image = image[top:bottom, left:right]
  img = Image.fromarray(face_image)
  display(img)