import json

'''
1. Convert json string to dict
'''

x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
print(type(y))
print(y)

'''
2. Convert dict to json string
'''
# a Python object (dict):
a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
b = json.dumps(a)

# the result is a JSON string:
print(type(b))
print(b)

'''
3. Other variable type also can convert to json string
'''
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
4. Add parameter when convert object to string json
'''

object_data = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json_result = json.dumps(object_data, sort_keys=True) # Can order the key in json
print(type(json_result))
print(json_result)