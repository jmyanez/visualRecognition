import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='3995db77bd70aa498157544096c84c5741b30668')


filename = raw_input("Some input please: ")


with open(filename, 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        classifier_ids='humans_1546902740')
    print(json.dumps(classes, indent=2))