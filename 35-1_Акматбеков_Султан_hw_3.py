class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        result = self.__cpu + self.__memory
        print(f"Computations result: {result}")

    def __str__(self):
        return f"Computer (CPU: {self.__cpu}, Memory: {self.__memory})"

    def __eq__(self, other):
        return self.__memory == other.get_memory()

    def __ne__(self, other):
        return self.__memory != other.get_memory()

    def __lt__(self, other):
        return self.__memory < other.get_memory()

    def __gt__(self, other):
        return self.__memory > other.get_memory()

    def __le__(self, other):
        return self.__memory <= other.get_memory()

    def __ge__(self, other):
        return self.__memory >= other.get_memory()


class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Calling number {call_to_number} from SIM card {sim_card}")

    def __str__(self):
        return f"Phone (SIM Cards: {self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)

    def use_gps(self, location):
        print(f"Calculating route to {location}")

    def __str__(self):
        return f"SmartPhone (CPU: {self.get_cpu()}, Memory: {self.get_memory()}, SIM Cards: {self.get_sim_cards_list()})"


computer = Computer("Intel i5", 8)
phone = Phone()
smartphone1 = SmartPhone("Snapdragon", 4)
smartphone2 = SmartPhone("Exynos", 6)

computer.set_cpu("Intel i7")
phone.set_sim_cards_list(["Beeline", "Megacom", "O!"])

computer.make_computations()
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Home")
smartphone2.use_gps("Office")

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer == smartphone1)  
print(computer != smartphone2)
print(smartphone1 < smartphone2)
print(smartphone2 > computer)
print(smartphone1 <= smartphone2)
print(computer >= smartphone1)