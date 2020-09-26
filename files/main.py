import json

with open('abc.json', 'r') as file:
    d1json = file.read()
    d1json = json.loads(d1json)

for k, v in d1json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
