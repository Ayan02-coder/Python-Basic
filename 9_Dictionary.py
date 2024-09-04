# dict = {
#     "name" : "Ayan",
#     "age" : 21,
#     "cgpa" : 8.9,
#     "subject" : ["python","Networking","Cyber security"],
#     "topics" : ("Dict","set")
# }
# print(type(dict))
# print(dict["subject"])
# dict["name"] = "Sayyad"
# print(dict["name"])
# dict["surnmae"] = "Ayan"
# print(dict)


## Nested Dictionary
# student = {
#     "name":"Ayan",
#     "subject":{
#         "chem":97,
#         "phy":96,
#         "math":97
#     }
# }

# print(student)
# print(student["subject"])
# print(student["subject"]["math"])

## Methods
student = {
    "name":"Ayan",
    "subject":{
        "chem":97,
        "phy":96,
        "math":97
    }
}

print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))
print(len(student.keys()))

print(student.values())

print(student.items())

print(student["name"])
print(student.get("name"))
print(student.get("name1"))

student.update({"city" : "pune"})
print(student)
