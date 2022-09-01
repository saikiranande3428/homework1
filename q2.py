dog = {"name":"Chotu", "color":"Black", "breed":"Rottwiller", "legs":4, "age":3}
student = { "first_name":"Sai Kiran", "last_name":"Ande", "gender":"male", "age":25, "marital_status":"Unmarried", "skills":["Python","ML","Java","AI"], "country":"India", "city":"Vijayawada", "address":"Poranki"}

print(len(student))
print(student["skills"],type(student["skills"]))
student["skills"].append("Pulihora")
student["skills"].append("Cooking")
print(student.keys())
print(student.values())
