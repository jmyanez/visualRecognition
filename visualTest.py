import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='3995db77bd70aa498157544096c84c5741b30668')

with open('./pata.zip', 'rb') as human, open('./cats.zip', 'rb') as cats:
    model = visual_recognition.create_classifier(
        'humans',
        human_positive_examples=human,
        negative_examples=cats)
print(json.dumps(model, indent=2))