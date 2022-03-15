import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file('F:\programming\face recognition\image\rickastley.png')
face_landmarks = face_recognition.face_landmarks(image)

img = Image.fromarray(image)

for i in face_landmarks:
  d = ImageDraw.Draw(img, 'RGBA')

  d.polygon(i['left_eyebrow'], fill=(68, 54, 39, 128))
  d.polygon(i['right_eyebrow'], fill=(68, 54, 39, 128))
  d.line(i['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
  d.line(i['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

  d.polygon(i['top_lip'], fill=(150, 0, 0, 128))
  d.polygon(i['bottom_lip'], fill=(150, 0, 0, 128))
  d.line(i['top_lip'], fill=(150, 0, 0, 64), width=8)
  d.line(i['bottom_lip'], fill=(150, 0, 0, 64), width=8)

  d.line(i['left_eye'] + [i['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
  d.line(i['right_eye'] + [i['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

  display(img)
