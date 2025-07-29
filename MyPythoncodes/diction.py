student = {
  "aami":{  "name": "John",
    "age": 21,
    "major": "Computer Science",
    "grades": [85, 92, 78],},
}


student["aami"]["grades"].append(89)


student.update({"irfana":{  "name": "minu",
    "age": 21,
    "major": "Computer Science",
    "grades": [100, 100, 78],}})
    
    
print(student["aami"])
print(student["irfana"])


dictionary={}
dictionary["009"]={  "name": "John",
    "age": 21,
    "major": "Computer Science",
    "grades": [85, 92, 78],}
print(dictionary)