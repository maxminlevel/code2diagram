import json

obj = '{"attribute": {"name": "Simple","type": "Usecase"},"data": [{"name": "Man","uniq": "1","type": "actor","group": "","attribute": ""},{"name": "do some thing","uniq": "2","type": "usecase","group": "","attribute": ""},{"source": 1,"target": 2,"attribute": {"type": ""}}]}'
data = json.loads(obj)

print(data)
print(type(data))

print(data['attribute'])