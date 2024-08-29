person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 25,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print("Middle skill:", middle_skill)
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('Unknown title')
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")
