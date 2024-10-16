
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

em1 = employee( "Baker", "smadi", 1000, "111-22-3333", "M")
em2 = employee("John", "smith", 1500, "999-99-9999", "M")

print(em1.__dict__)
em1.fun()
print(em1.salary)
print(em2.salary)
em2.fun()
print(em2.salary)