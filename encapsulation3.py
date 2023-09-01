class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project
    def work(self):
        return self.name, self.salary, self.project
    def designation(self, designation):
        self.designation = designation
        if self.project:
            return self.name, self.salary, self.project, self.designation
        else:
            return self.name, self.salary


emp = Employee("Albert", "500k", "Blackholes", "Scientist")
print(emp.designation())