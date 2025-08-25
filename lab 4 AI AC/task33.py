def extract_student_info(student_dict):
    """
    Extracts full name, branch, and SGPA from a nested student dictionary.
    Returns a tuple: (full_name, branch, sgpa)
    """
    full_name = student_dict.get('name', {}).get('first', '') + ' ' + student_dict.get('name', {}).get('last', '')
    branch = student_dict.get('branch', '')
    sgpa = student_dict.get('academics', {}).get('SGPA', None)
    return full_name.strip(), branch, sgpa

# Example student dictionaries
student1 = {
    'name': {'first': 'Amit', 'last': 'Sharma'},
    'branch': 'CSE',
    'academics': {'SGPA': 8.7, 'year': 2}
}

student2 = {
    'name': {'first': 'Priya', 'last': 'Verma'},
    'branch': 'ECE',
    'academics': {'SGPA': 9.1, 'year': 3}
}

student3 = {
    'name': {'first': 'Rahul', 'last': 'Singh'},
    'branch': 'ME',
    'academics': {'SGPA': 7.8, 'year': 1}
}

# Using the function with examples
for student in [student1, student2, student3]:
    name, branch, sgpa = extract_student_info(student)
    print(f"Name: {name}, Branch: {branch}, SGPA: {sgpa}")