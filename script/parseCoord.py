import json

with open('1.txt', 'r', encoding='utf-8-sig') as f:
    str = f.read()

    dict_str = json.loads(str)

    features = dict_str['features']

    for feature in features:
        properties = feature['properties']
        geometry = feature['geometry']
        if geometry['type'] == 'LineString' and len(geometry['coordinates']) <= 1:
            print(properties['name'])

