#Classe voo
class Flight:

    counter = 1


    def __init__(self, origin, destination, duration):
        
        #gerencia o id
        self.id = Flight.counter
        Flight.counter += 1

        #gerencia os passageiros
        self.passangers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration
    

    def print_info(self):

        #informações de voo
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()

        #informações dos passageiros
        print("Passagers: ")
        for passanger in self.passangers:
            print(f"{passanger.name}")


    def delay(self, amount):
        self.duration += amount
    

    def add_passanger(self, p):
        self.passangers.append(p)
        p.flight_id = self.id



#Classe passageiro
class Passenger:

    def __init__(self, name):
        self.name = name



#Função principal
def main():
    f = Flight(origin="New York", destination="Paris", duration= 540)
    
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    f.add_passanger(alice)
    f.add_passanger(bob)

    f.print_info()

if __name__ == "__main__":
    main()