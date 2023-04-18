import json

x = '{"name": "Prince", "age": 17, "class":"grade 7"}'
print(x)

y = json.loads(x)

print(y)

print(json.dumps(y, indent=4, sort_keys=True, separators=(" . ", " =")))