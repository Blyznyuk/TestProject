class Person:
  def __init__(self, name, sername="Doe", famil="hz"):
        if not name:
            self.name = "John"
        else:
            self.name = name
        if not sername:
            self.sername = "Doe"
        else:
            self.sername = sername
        if not famil:
            self.famil = "noone"
        else:
            self.famil = famil
        self.age = []


# class Person_age:
#     def __init__(self, name, sername, famil, years):
#         self.name = name
#         self.famil = famil
#         self.sername = sername
#         self.years = years
#        # return print(name, sername, famil, sep=' ')
#
#     def age_return(self, age):
#         self.years += age
#         return print(self.years, self.name, self.sername, self.famil, sep=' ')

class Personage:
    def __init__(self, name = None, sername = None, famil = None, years = None):
        self.name = name
        self.famil = famil
        self.sername = sername
        self.years = years
       # return print(name, sername, famil, sep=' ')

    def age_return(self, age):
        self.years += age
        return print(self.famil, self.name, self.sername, self.years, "old", sep=' ', end=' ')


class Employer(Personage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = None

    def employers(self, position):
        self.position = position
        print("work as", position, sep=' ', end=' ')


if __name__ == '__main__':
    # p1 = Person(input("name: "), input("Sername: "), input("Fmiliya: "))
    # print(p1.famil, p1.name, p1.sername)
    # p2 = Person2(input("name: "), input("Sername: "), input("Fmiliya: "))

    name = input("name: ")
    sername = input("Sername: ")
    famil = input("Fmiliya: ")
    years = int(input("age: "))
    # p3 = Person_age(name, sername, famil, years)
    # p3.age_return(10)

    p4 = Employer(name, sername, famil, years)
    p4.age_return(25), p4.employers("QA")




