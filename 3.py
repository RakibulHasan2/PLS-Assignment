from enum import Enum
# Define an enumeration
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum values
print(f"Color Red: {Color.RED}")
print(f"Color Green Value: {Color.GREEN.value}")
