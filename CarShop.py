from abc import abstractmethod, ABC
from dataclasses import dataclass
from enum import Enum


class FuelType(Enum):
    PETROL = 1
    DIESEL = 2
    ELECTRIC = 3


@dataclass
class Vehicle(ABC):
    wheels: int
    colour: str
    doors: int
    manufacturer: str
    max_speed: float
    fuel: FuelType

    def drive(self):
        print("Drive!")

    @abstractmethod
    def open_doors(self):
        print("Hinge Front Handle Back")

    def refuel(self):
        print(F"Top up your {self.fuel.name}.")

    @abstractmethod
    def park(self):
        print("Park the car yourself.")


@dataclass
class Car(Vehicle):

    def open_doors(self):
        super().open_doors()

    def park(self):
        print("Use the park button.")


@dataclass
class Van(Vehicle):

    def open_doors(self):
        print("Sliding on Rails")

    def park(self):
        print("Drive forwards.")


@dataclass
class Lorry(Vehicle):
    def open_doors(self):
        print("Big Side and Rear")

    def park(self):
        print("Reverse with trailer.")


def do_vehicle_actions(given_vehicle: Vehicle):
    print(type(given_vehicle))
    print(given_vehicle)
    given_vehicle.open_doors()
    given_vehicle.park()
    given_vehicle.drive()
    given_vehicle.refuel()


if __name__ == "__main__":
    depnecy = "This is my depency"
    list_of_vehicles: list[Vehicle] = []
    for i in range(0, 3):
        list_of_vehicles.append(Car(i + 2, "Red", i + 3, "DLC", i * 100, FuelType(i + 1)))

    for i in range(3, 6):
        list_of_vehicles.append(Van(i + 2, "White", i + 3, "DLC", i * 80, FuelType(i - 2)))

    for i in range(6, 9):
        list_of_vehicles.append(Lorry((i * 2) + 2, "Green", i + 3, "DLC", i * 50, FuelType(i - 5)))

    for vehicle in list_of_vehicles:
        do_vehicle_actions(vehicle)
