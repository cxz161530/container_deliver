#Exercise 1
students = ['John', 'Jinah', 'Ross', 'Kevin']
#print second student
print(students[1])
#print last student
print(students[-1])

#Exercise 2
foods=('apple','banana', 'pineapple', 'strawberry')

for food in foods:
    print(f"{food} is a good food")

#Exercise 3
for food in foods:
    print(food[-2:])

#Exercise 4
home_town = {
    'city': 'Shanghai',
    'state': 'China',
    'population': 10000
}

print (f"I was born in {home_town.get('city')}, {home_town.get('state')}- population of {home_town.get('population')}")

#Exercise 5
for key, val in home_town.items():
  print( f"{key} = {val}" )

#Exercise 6:
cohort=[]


for index, student in enumerate (students):
    dic = {}
    dic['student']=student
    dic['fav_food']=foods[index]
    cohort.append(dic)
print(cohort)

#Exercise 7
awesome_students = [f"{student} is awesome!" for student in students]
for student in awesome_students:
    print(student)

#Exercise 8
foods_tuple  = tuple(foods)
foods_final = []
for food in foods_tuple:
    if 'a' in food:
        foods_final.append(food)
foods_final = tuple(foods_final)
        
print(foods_final)

