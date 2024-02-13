from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Person:
    first_name: str
    last_name: str
    start_date: datetime


@dataclass
class TemporaryPerson(Person):
    end_date: datetime


@dataclass
class Student(TemporaryPerson):
    class_name: str


@dataclass
class Staff(TemporaryPerson):
    building_name: str

    def __post_init__(self):
        self.contract_length = self.end_date - self.start_date


@dataclass
class Visitor(Person):
    visit_person: str


@dataclass
class Teacher(Person):
    building_name: str
    class_name: str


if __name__ == "__main__":
    student1 = Student("John", "Smith", datetime(2021, 9, 7), datetime(2026, 7, 27), "Biology")
    staff1 = Staff("James", "Small", datetime(2020, 9, 6), datetime(2024, 7, 24), "Science Building")
    visitor1 = Visitor("Jason", "Sandon", datetime(2022, 11, 10), "John Smith")
    teacher1 = Teacher("Jack", "Stard", datetime(2021, 9, 7), "Science Building", "Biology")
    print(student1)
    print(staff1)
    print(visitor1)
    print(teacher1)
