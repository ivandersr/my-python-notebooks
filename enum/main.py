from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise TypeError('invalid direction')
    return f'Moving {direction.name}'


print(move(Directions.right))
print(move(Directions.left))
print(move(Directions.up))
print(move(Directions.down))

for direction in Directions:
    print(direction.value, direction.name)
