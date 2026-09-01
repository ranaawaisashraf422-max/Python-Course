student = {
    "name": "Awais",
    "age": 20,
    "city": "Faisalabad"
}

#Clear Method
print(student.clear())

#copy Method
print(student.copy())

#fromkeys Method
print(student.fromkeys(["A","B","C"],0))

#get Method
print(student.get("name"))

#items Method
print(student.items())

#keys method
print(student.keys())

#pop Method
print(student.pop("city"))

#popitem method
print(student.popitem())

#setdefault Method
print(student.setdefault("Country","India"))

#update Method
print(student.update({"age": 21, "gender": "Male"}))
print(student)

#values Method
print(student.values())

