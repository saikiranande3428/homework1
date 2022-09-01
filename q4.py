it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of it_companies =",len(it_companies))

it_companies.add("Twitter")

it_companies.update({"TCS","Accenture"})

it_companies.remove("Accenture")

print(A|B)
print(A.intersection(B))
print(A.issubset(B))
print(A.symmetric_difference(B))
del A,B
age_set = set(age)
print(len(age_set)<len(age))
#print(it_companies)