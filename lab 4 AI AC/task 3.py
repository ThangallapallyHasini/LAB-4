class Student:
    def __init__(self, fullname, branch, sgpa):
        self.fullname = fullname
        self.branch = branch
        self.sgpa = sgpa

    def show(self):
        return f"Name: {self.fullname}, Branch: {self.branch}, SGPA: {self.sgpa}"

def create_student(fullname, branch, sgpa):
    return Student(fullname, branch, sgpa)

# Few-shot examples
student1 = create_student("Alice Johnson", "CSE", 9.1)
student2 = create_student("Bob Smith", "ECE", 8.7)

print(student1.show())
print(student2.show())