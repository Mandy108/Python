# Class: class is a blueprint or a template. Eg. From for an exam that contains name, age, electives, father's name etc.

# Object: Specific instance created from the template(class) . Eg. form which contains data from john

class Employee:
    company = "Adobe"

    def get_salary(self): # Self is important here because self is a way to reference the object of the class which is being created
       
        return 34000

a = Employee() # An object of class employee is created here
print(a.get_salary()) # Employee e's get_salary method is called
a2 = Employee()
print(a2.get_salary())
print(a2.company)