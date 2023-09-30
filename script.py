from typing import override

class Animal:
    def make_sound(self) -> str:
        return "some sound"

class Dog(Animal):
    @override  # ok: overrides Animal.make_sound
    def make_sound(self) -> str:
        return "bark"

class Cat(Animal):
    @override  # Type checker error: does not override Animal.make_sound
    def make_noise(self) -> str:
        return "meow"
