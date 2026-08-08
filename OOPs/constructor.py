class employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # created an instance attribute of an name of a salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name of the employee {self.name}. salary of the employee {self.salary}Rupees. Bond of the employee {self.bond}years.")

a = employee(34000, "john", 4)
print(a.get_salary())
a.get_info()