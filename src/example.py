from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Person:
    name: str
    age: int


def generate_person() -> Person:
    return Person(name="John", age=30)


Book = TypedDict("Book", {"title": str, "author": str})


def generate_book() -> Book:
    return {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}


def add(a: int, b: int) -> int:
    return a + b


class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.__make = make
        self.__model = model
        self.__year = year

    def __str__(self) -> str:
        return f"The vehicle is a {self.__year} {self.__make} {self.__model}"


def main() -> None:
    person = generate_person()
    print(f"The person {person.name} is {person.age} years old")

    book = generate_book()
    print(f"The book is {book['title']} by {book['author']}")

    vehicle = Vehicle(make="Toyota", model="Corolla", year=2020)
    print(vehicle)

    result = add(1, 2)
    print(result)


if __name__ == "__main__":
    main()
