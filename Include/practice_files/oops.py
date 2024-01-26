class computer1:

    def data(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def d2(self):
        return self.storage

    def compare(self, other):
        if self.ram == other.ram:
            return True
        else:
            return False


class computer2:

    screen = 15

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def info(cls):
        return cls.screen

    @staticmethod
    def info_():
        return ("the static method...")


c1 = computer1()
c1.data(4, '512GB')
c2 = computer2(8, '1TB')
print(c2.ram)
print(c1.d2)
print(c1.compare(c2))
print(computer2.info())
print(computer2.info_())


class student:

    def __init__(self, name, standard):
        self.name = name
        self.standard = standard
        self.lap = self.laptop

    class laptop:

        def __init__(self, brand, ram):
            self.brand = brand
            self.ram = ram


s1 = student("abc", 10)
s2 = student("dsa", 11)

# l1 = student.laptop("asus", 8)
# l2 = student.laptop("dell", 4)

lap1 = s1.lap("asus", 8)
lap2 = s2.lap("dell", 4)

print(lap1.brand)
