students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def candies(dict):
    names = []
    candies = 0
    for i in range(len(dict)):
        names.append(students[i]['name'])
        #print(names)
        if students[i]['age'] < 10:
            names.append(students[i]['candies'])
            candies = candies + students[i]['candies']

    print(names)
    print(candies)

candies(students)
