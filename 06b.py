import json
file = open("json_example.txt","w")
file.write(json.dumps({'imie': 'marcin', 'nazwisko': 'hajdo'}))
file = open("json_example.txt","r")
file_content = file.read()
json_content = json.loads(file_content)
json_content["imie"] = "xxx"
str_content = json.JSONEncoder().encode(file_content)
print(str_content)
