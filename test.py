import json
from watson_developer_cloud import VisualRecognitionV3


visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='3995db77bd70aa498157544096c84c5741b30668')


with open('./pedestrian.jpg', 'rb') as images_file:
    faces = visual_recognition.detect_faces(images_file)
print(json.dumps(faces, indent=2))