import arrow
from collections import namedtuple

print("Chapter 11: Advanced Dictionary Operations")
arrow.now().format()  # just to use the arrow import

brewing_time = arrow.utcnow()
print(brewing_time)
print(brewing_time.to("Europe/London"))

chaiProfile = namedtuple("ChaiProfile", ["type", "size", "sugar"])
print(chaiProfile("Masala Chai", "Large", 2))
print(chaiProfile(type="Ginger Chai", size="Medium", sugar=1))