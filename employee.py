
class employee:
    tax = 0.10
    def __init__(self, f_name, l_name, salary, ssn, gender,):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.ssn = ssn
        self.gender = gender
        self.email = self.f_name+"_"+self.l_name+"@gmail.com"
    def fun(self):
        self.salary = self.salary - self.salary * self.tax

class supervisor(employee):
    def __init__(self, f_name, l_name, salary, ssn, gender, employees = None):
        super().__init__(f_name, l_name, salary, ssn, gender)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print(emp.f_name+", "+ emp.l_name)


em1 = employee( "Baker", "smadi", 1000, "111-22-3333", "M")
em2 = employee("John", "smith", 1500, "999-99-9999", "M")
sup1 = supervisor("mike", "smite", 2000, "555-33-4444", "M", ["baker"])
sup1.add_emp(em1)
sup2 = supervisor("jad", "Jordan", 5000, "99-77-8766", "M", [em2])
sup1.add_emp(em2)
sup1.print_emp()

#print(sup1.__dict__)
#em1.fun()
#print(em1.salary)
#print(em2.salary)
#em2.fun()
#print(em2.salary)