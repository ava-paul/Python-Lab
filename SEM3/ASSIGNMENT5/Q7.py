student = {
    'first_name': 'Ava',
    'last_name': 'Paul',
    'gender': 'Female',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Node Js', 'Java'],
    'country': 'India',
    'city': 'Kolkata',
    'address': 'Belgharia'
}
length_of_student_dict = len(student)
print("Length of the student dictionary:", length_of_student_dict)
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))
student['skills'].extend(['Python', 'Backend Development'])
print("Modified skills:", student['skills'])
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)
values_list = list(student.values())
print("Dictionary values:", values_list)
student_items = list(student.items())
print("List of tuples (items):", student_items)
del student['marital_status']
print("Dictionary after deleting 'marital_status':", student)
del student
try:
    print(student)
except NameError:
    print("The student dictionary has been deleted.")
