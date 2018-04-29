import json
from watson_developer_cloud import VisualRecognitionV3


visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='3995db77bd70aa498157544096c84c5741b30668')


with open('./apie.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters = json.dumps({
            'classifier_ids': ["humans_718172774"]
        }))
print(json.dumps(classes, indent=2))