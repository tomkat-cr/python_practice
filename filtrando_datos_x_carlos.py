# File: filtrando_datos_x_carlos.py

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    # adults =  [worker["name"] for worker in DATA if worker["age"] > 18]

    # New map/filter solutions
    all_python_devs = list(filter(lambda worker : worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker : worker["name"], all_python_devs))

    all_Platzi_workers = list(filter(lambda worker : worker["organization"] == "Platzi", DATA))
    all_Platzi_workers = list(map(lambda worker : worker["name"], all_Platzi_workers))

    adults = list(filter(lambda worker : worker["age"] > 18, DATA))
    adults = list(map(lambda worker : worker['name'], adults))

    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # New comprehensions solutions

    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]

    print()
    print('1) all_python_devs')
    for worker in all_python_devs:
        print(worker)

    print()
    print('2) all_Platzi_workers')
    for worker in all_Platzi_workers:
        print(worker)

    print()
    print('3) Adults')
    for adult in adults:
        print(adult)

    print()
    print('4) Old people (all)')
    for old_person in old_people:
        print(old_person)

    print()
    print('4) Old people (filtered)')
    print(list(filter(lambda person : person['old'] == True, old_people)))


if __name__ == '__main__':
    run()
