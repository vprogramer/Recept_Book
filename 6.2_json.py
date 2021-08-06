import json


data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# json_str = json.dumps(data)

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)

print(data, type(data))


from collections import OrderedDict

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data_s = json.loads(s, object_pairs_hook=OrderedDict)
print(data_s)
