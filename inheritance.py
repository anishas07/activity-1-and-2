class person:
    def __init__(self,name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("The person is", self.name)
        print("The idnumber is", self.idnumber)
    
class employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.salary = post
        person.__init__(self, name, idnumber)
object1 =employee("Jess", 30, 60000, "manager")
object1.display()