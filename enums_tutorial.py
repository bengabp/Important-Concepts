from enum import Enum


"""Enums are objects in python that has a fixed value."""


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    PARTIALLY_ACTIVE = 0.5
    COMPLETELY_INACTIVE = -0.5

    def __call__(self, *args, **kwargs):
        print("Calling")
        return self.value

    def __repr__(self):
        return f"Enum(State)<{self.name}:{self.value}>"

    def __str__(self):
        return f"Enum(State)<{self.name}:{self.value}>"


# Getting the value of an enum
inactive_state = State.INACTIVE
print(f"Inactive state = {inactive_state.value} and type is {type(inactive_state)}")

# Getting all available enums in a class
available_enums = list(State)
print(f"Available enums are {available_enums}")

