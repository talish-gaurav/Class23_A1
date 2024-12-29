
student_data = {
    "id1" : {"name" : ['Sara'], "class" : ["V"],"subject-intergration" : ["english, maths, science"]},
    "id2" : {"name" : ['David'], "class" : ["V"],"subject-intergration" : ["english, maths, science"]},
    "id1" : {"name" : ['Sara'], "class" : ["V"],"subject-intergration" : ["english, maths, science"]},
    "id1" : {"name" : ['Surya'], "class" : ["V"],"subject-intergration" : ["english, maths, science"]},
}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)